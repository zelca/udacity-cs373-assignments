from matrix import *
from robot import *

# initial uncertainty: uncertain about everything
P_initial = matrix([[1000., 0., 0., 0., 0.],
                    [0., 1000., 0., 0., 0.],
                    [0., 0., 1000., 0., 0.],
                    [0., 0., 0., 1000., 0.],
                    [0., 0., 0., 0., 1000.]])


# transition matrix (Jacobian)
def F_matrix(state):
    h = state.value[2][0]
    t = state.value[3][0]
    d = state.value[4][0]

    return matrix([[1., 0., -d * sin(h + t), -d * sin(h + t), cos(h + t)],
                   [0., 1., d * cos(h + t), d * cos(h + t), sin(h + t)],
                   [0., 0., 1., 1., 0.],
                   [0., 0., 0., 1., 0.],
                   [0., 0., 0., 0., 1.]])


# new state function
def f(state):
    x = state.value[0][0]
    y = state.value[1][0]
    h = state.value[2][0]
    t = state.value[3][0]
    d = state.value[4][0]

    h += t
    x += d * cos(h)
    y += d * sin(h)

    return matrix([[x], [y], [h], [t], [d]])


# measurement function: reflect the fact that we observe everything except turning
H = matrix([[1., 0., 0., 0., 0.],
            [0., 1., 0., 0., 0.],
            [0., 0., 0., 0., 1.]])


# measurement uncertainty
def R_matrix(sigma):
    return matrix([[sigma, 0., 0.],
                   [0., sigma, 0.],
                   [0., 0., sigma ** 2]])


# 4d identity matrix
I = matrix([[1., 0., 0., 0., 0.],
            [0., 1., 0., 0., 0.],
            [0., 0., 1., 0., 0.],
            [0., 0., 0., 1., 0.],
            [0., 0., 0., 0., 1.]])

# external motion: no external motion
u = matrix([[0.], [0.], [0.], [0.], [0.]])


class ExtendedKalmanFilter:
    def __init__(self, sigma):
        self.P = P_initial
        self.R = R_matrix(sigma)
        self.x = matrix([[0.], [0.], [0.], [0.], [0.]])

    def localize(self, Z):
        """Applies Extended Kalman Filter for given x and P"""

        x = self.x
        P = self.P
        R = self.R

        # measurement update
        y = Z.transpose() - (H * x)
        S = H * P * H.transpose() + R
        K = P * H.transpose() * S.inverse()
        x = x + (K * y)
        P = (I - (K * H)) * P

        # prediction
        F = F_matrix(x)
        P = F * P * F.transpose()
        x = f(x)

        self.x = x
        self.P = P

        return x
