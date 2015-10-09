deviation = 0.02 / s
p = 1 - 2*(1 - st.norm.cdf(deviation))
print "probability: {0:.4f}".format(p)