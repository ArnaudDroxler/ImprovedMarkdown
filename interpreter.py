import AST

if __name__ == "__main__":

    import sys
    import os

    #import .parser.parse as parse
    from parser import parse
    #from threader import thread
    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    #entry = thread(ast)

    name = os.path.splitext(sys.argv[1])[0]+'.html'

    html = open(name)
    html.write("coucou")


    #execute(entry)
    html.close()
