from glpk.glpkpi import *

def abs(f_name, tmlim=3600000, memlim=1024, w2ascii=True, w2pickle=False, debug=False):
    """Build and solve the model.
    
    :param f_name: name of pickle file with data.

    :type f_name: string.
    
    :param tmlim: time limit, in milliseconds.

    :type tmlim: integer, default 3600000.

    :param memlim: memory limit, in megabytes.

    :type memlim: integer, default 1024.

    :param w2ascii: write the solution to a ASCII file.

    :type w2ascii: boolean, default True.

    :param w2pickle: write the solution to a pcikle file.

    :type w2pickle: boolean, default False.

    :param debug: enable the debug behavior.

    :type debug: boolean.
    """
    import pickle

    if debug:
        print("Debug mode enable.")

    print("Try to load data from {0}.".format(f_name))
    with open(f_name, 'rb') as f:
        print("Load {0}.".format(f_name))
        data = pickle.load(f)
    print("Data sucessfully load from {0}.".format(f_name))

    len_j = len(data['j'])
    len_a = len(data['a'])
    ind = intArray(len_j + len_a + 1)
    val = doubleArray(len_j + len_a + 1)
    prob = glp_create_prob()
    glp_create_index(prob)

    glp_add_rows(prob, len_j + len_a)
    for i in xrange(len_j):
        glp_set_row_name(prob, i + 1, "J{0}".format(data['j'][i]))
        glp_set_row_bnds(prob, i + 1, GLP_UP, 0.0, data['phi'][i])
    for i in xrange(len_a):
        glp_set_row_name(prob, len_j + i + 1, "A{0}".format(data['a'][i]))
        glp_set_row_bnds(prob, len_j + i + 1, GLP_UP, 0.0, data['psi'][i])

    glp_set_obj_dir(prob, GLP_MAX)
    for path in data['p']:
        count = 0
        col = glp_add_cols(prob, 1)
        glp_set_col_name(prob, col, "{0}".format(path))
        glp_set_col_bnds(prob, col, GLP_LO, 0.0, 0.0)
        for k in xrange(len_j):
            if path[0] == data['j'][k][0] and path[1] == data['j'][k][1]:
                count = count + 1
                ind[count] = glp_find_row(prob, "J{0}".format(data['j'][k]))
                val[count] = data['phi'][k]
        for k in xrange(len_a):
            if path[2] == data['a'][k][0] and path[3] == data['a'][k][1]:
                count = count + 1
                ind[count] = glp_find_row(prob, "A{0}".format(data['a'][k]))
                val[count] = data['psi'][k]
        glp_set_mat_col(prob, col, count, ind, val)
        glp_set_obj_coef(prob, col, 1.0)

    if debug:
        glp_write_lp(prob, None, f_name.replace(".pickle", ".lp"))
    else:
        glp_mem_limit(memlim)
        param = glp_smcp()
        glp_init_smcp(param)
        param.tm_lim = tmlim
        glp_simplex(prob, param)
        z = glp_get_obj_val(prob)
        if w2ascii:
            print("Try to write solution in {0}.".format(
                    f_name.replace(".pickle", ".txt")))
            with open(f_name.replace(".pickle", ".txt"), 'wb') as f:
                for j in xrange(1, glp_get_num_cols(prob) + 1):
                    aux = glp_get_col_prim(prob, j)
                    if aux > 0:
                        f.write("{0} {1}\n".format(glp_get_col_name(prob, j),
                                aux))
            print("Solution sucessfully write in {0}.".format(
                    f_name.replace(".pickle", ".txt")))
        if w2pickle:
            x = []
            for j in xrange(1, glp_get_num_cols(prob) + 1):
                x.append(glp_get_col_prim(prob, j))
            print("Try to write solution in {0}.".format(
                    f_name.replace(".pickle", ".spickle")))
            with open(f_name.replace(".pickle", ".spickle"), 'wb') as f:
                pickle.dump({"z": z, "x": x}, f)
            print("Solution sucessfully write in {0}.".format(
                    f_name.replace(".pickle", ".spickle")))
    del prob
    return z

def rbs(f_name, tmlim=3600000, memlim=1024, w2ascii=True, w2pickle=False, debug=False):
    """Build and solve the model.
    
    :param f_name: name of pickle file with data.

    :type f_name: string.
    
    :param tmlim: time limit, in milliseconds.

    :type tmlim: integer, default 3600000.

    :param memlim: memory limit, in megabytes.

    :type memlim: integer, default 1024.

    :param w2ascii: write the solution to a ASCII file.

    :type w2ascii: boolean, default True.

    :param w2pickle: write the solution to a pcikle file.

    :type w2pickle: boolean, default False.

    :param debug: enable the debug behavior.

    :type debug: boolean.
    """
    import pickle

    if debug:
        print("Debug mode enable.")

    print("Try to load data from {0}.".format(f_name))
    with open(f_name, 'rb') as f:
        print("Load {0}.".format(f_name))
        data = pickle.load(f)
    print("Data sucessfully load from {0}.".format(f_name))

    len_j = len(data['j'])
    len_a = len(data['a'])
    ind = intArray(len_j + len_a + 1)
    val = doubleArray(len_j + len_a + 1)
    prob = glp_create_prob()
    glp_create_index(prob)

    glp_add_rows(prob, len_j + len_a)
    for i in xrange(len_j):
        glp_set_row_name(prob, i + 1, "J{0}".format(data['j'][i]))
        glp_set_row_bnds(prob, i + 1, GLP_UP, 0.0, data['phi'][i])
    for i in xrange(len_a):
        glp_set_row_name(prob, len_j + i + 1, "A{0}".format(data['a'][i]))
        glp_set_row_bnds(prob, len_j + i + 1, GLP_UP, 0.0, data['psi'][i])

    glp_set_obj_dir(prob, GLP_MAX)
    for path in data['p']:
        if path[4]:
            count = 0
            col = glp_add_cols(prob, 1)
            glp_set_col_name(prob, col, "{0}".format(path[0:4]))
            glp_set_col_bnds(prob, col, GLP_LO, 0.0, 0.0)
            for k in xrange(len_j):
                if path[0] == data['j'][k][0] and path[1] == data['j'][k][1]:
                    count = count + 1
                    ind[count] = glp_find_row(prob, "J{0}".format(data['j'][k]))
                    val[count] = data['phi'][k]
            for k in xrange(len_a):
                if path[4] == data['a'][k][0] and path[5] == data['a'][k][1]:
                    count = count + 1
                    ind[count] = glp_find_row(prob, "A{0}".format(data['a'][k]))
                    val[count] = data['psi'][k]
            glp_set_mat_col(prob, col, count, ind, val)
            glp_set_obj_coef(prob, col, 1.0)

    if debug:
        glp_write_lp(prob, None, f_name.replace(".pickle", ".lp"))
    else:
        glp_mem_limit(memlim)
        param = glp_smcp()
        glp_init_smcp(param)
        param.tm_lim = tmlim
        glp_simplex(prob, param)
        z = glp_get_obj_val(prob)
        if w2ascii:
            print("Try to write solution in {0}.".format(
                    f_name.replace(".pickle", ".txt")))
            with open(f_name.replace(".pickle", ".txt"), 'wb') as f:
                for j in xrange(1, glp_get_num_cols(prob) + 1):
                    aux = glp_get_col_prim(prob, j)
                    if aux > 0:
                        f.write("{0} {1}\n".format(glp_get_col_name(prob, j),
                                aux))
            print("Solution sucessfully write in {0}.".format(
                    f_name.replace(".pickle", ".txt")))
        if w2pickle:
            x = []
            for j in xrange(1, glp_get_num_cols(prob) + 1):
                x.append(glp_get_col_prim(prob, j))
            print("Try to write solution in {0}.".format(
                    f_name.replace(".pickle", ".spickle")))
            with open(f_name.replace(".pickle", ".spickle"), 'wb') as f:
                pickle.dump({"z": z, "x": x}, f)
            print("Solution sucessfully write in {0}.".format(
                    f_name.replace(".pickle", ".spickle")))
    del prob
    return z
