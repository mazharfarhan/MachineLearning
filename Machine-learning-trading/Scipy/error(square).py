def error(line, data):
    # compute error between the line model and the obsereved data
    
    #line c1 and c2 coefficients
    err = np.sum((data[:, 1] - (line[0] * data[:, 0] + line[1]) ** 2 )
    return err
