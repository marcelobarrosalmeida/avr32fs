import sys

def printmsg(msg,nl=True):
    sys.stdout.write(msg)
    if nl: sys.stdout.write('\n')
    
def series2xml(package,patches):
    for p in patches:
        varname = package + '-' + p.replace('.','-')
        m = "<!ENTITY %s \"%s\">" % (varname,p)
        printmsg(m)

    for p in patches:
        varname = package + '-' + p.replace('.','-')
        printmsg("<patch>")
        printmsg("<param>-p1</param>")
        m = "<param>-i &packages_dir;/%s/&%s;</param>" % (package,varname)
        printmsg(m)
        printmsg("</patch>")
    
if __name__ == "__main__":
    if len(sys.argv) < 3:
        printmsg('Missing parameters !')
        printmsg("Syntax: %s package series_files" % sys.argv[0])
        sys.exit(1)

    try:
        patches = open(sys.argv[2]).readlines()
    except:
        printmsg('Error when opening file %s !' % sys.argv[2])
        sys.exit(1)

    # remove blank line and line endings
    patches = [ x.strip().replace('\n','') for x in patches if len(x) ]
    patches = [ x.strip().replace('\r\n','') for x in patches ]
    patches = [ x for x in patches if len(x) ]

    package = sys.argv[1]

    series2xml(package,patches)
      
