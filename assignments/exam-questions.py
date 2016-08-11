# Question 1: Probability
res = 1.0 / 6
print "Question 1:", res

# Question 2: Probability
prob_friday = .75
prob_if_rain = .6
prob_if_no_rain = .25
prob_saturday = prob_friday * prob_if_rain + (1 - prob_friday) * prob_if_no_rain
prob_sunday_if_saturday = prob_saturday * prob_if_rain
res = 1 - prob_sunday_if_saturday
print "Question 2:", res

# Question 3: Localization
measurements = ["g", "g", "r", "g", "r"]
input_prob = [.2, .2, .2, .2, .2]
measure_noise = .1
given = "r"
res = []
total = 0
for i in range(len(measurements)):
    correct = measurements[i] == given
    n = correct * (1 - measure_noise) * input_prob[i] + (1 - correct) * measure_noise * input_prob[i]
    res.append(n)
    total += n
for i in range(len(res)):
    res[i] = res[i] / total
print "Question 3:", res

# Question 4: Localization
# continues Question 3
input_prob = [0, res[0], res[1], res[2], res[3] + res[4]]
res = 0
for i in range(len(measurements)):
    correct = measurements[i] == given
    n = correct * (1 - measure_noise) * input_prob[i] + (1 - correct) * measure_noise * input_prob[i]
    res += n
print "Question 4:", res

# Question 5: Gaussians
mean1 = 1
var1 = 1
mean2 = 3
var2 = 1
new_mean = 1.0 / (var1 + var2) * (var2 * mean1 + var1 * mean2)
new_var = 1.0 / (1.0 / var1 + 1.0 / var2)
print "Question 5:", new_mean, new_var
