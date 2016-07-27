#! /usr/bin/env python

# WORKING BUT TO DOUBLE CHECK THE HTML OUTPUT

# Check data/test1.csv for input template

#### WARNING GOT LIMITATION:
# - numeric dtype should always have the max, min, step precised in
#the table. Or at least like "number:::"

# To add:
# Pattern for text type

#-------------------------------------------------------------------------------
def get_paras(tab_file):
    """
    From a tab delimited file with:
    $1: Program name
    $2: switches names in TRUFA
    $3: switches in the program integrated
    $4: type of data i.e. INT, STR, BOOL ...
    $5: description (which will appear on the webpage)

    Return a dctionnary by programs

    #### TYPE of data:
    Following html5:
    number:default:min:max:step
    text:default:pattern
    radio:opt1:opt2:opt3 ...
    """
    import csv

    par_d = {}

    with open(tab_file, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        
        for prog, name, switch, dtype, descr in reader:
            if prog in par_d:
                par_d[prog].append( (name, switch, dtype, descr) )
            else:
                par_d[prog] = [ (name, switch, dtype, descr) ]
            
        return par_d

#-------------------------------------------------------------------------------
def print_soft_data(tab_file):
    """
    Print out the dictionnary for soft_data.py 
    """
    print "arguments_dict = dict("    

    par_d = get_paras(tab_file)

    for prog in par_d:
        print "\t# PARAMS " + prog
        for paras in par_d[prog]:
            print "\t{0} = '{1}',".format(paras[0], paras[1])
        # The last extra "," does'nt seem to be a problem for python
    print ")"

#-------------------------------------------------------------------------------
def print_html(tab_file):
    """
    Print out the divs to insert in the html to incorporate the options
    Have to CHECK the collapses !!!
    paras[0] > name,
    paras[1] > switch,
    paras[2] > dtype,
    paras[3] > descr
    """
    
    par_d = get_paras(tab_file)
    count1 = 0
    for prog in par_d:
        count1 += 1
        collapse = "#collapseX_" + str(count1)
        count2 = 0
        
        print '<div class="accordion-group">'
        print '<div class="accordion-heading">'
        print '<a class="accordion-toggle" data-toggle="collapse" href="{}">'.format(collapse)
        print prog + ' options'
        print '</a>'
        print '</div>'
        print '<div id="{}" class="accordion-body collapse">'.format(collapse)
        print '<div class="accordion-inner">'

        for paras in par_d[prog]:
            count2 += 1
            input_id = prog + "_option" + str(count2)

            print '<div class="row">'
            print '<div class="control-group span3">'

            # Part specific to the type of data
            # Split to get the specification of max, min, step for number type
            ptype = paras[2].split(":")
            
            if ptype[0] == "number":

                print '<label class="control-label" for="{}">'.format(input_id)
                print paras[3] + ":"
                print '</label>'
                print '<div class="controls">'

                try:
                    print '<input id="{0}" type="number" value="{1}" min="{2}" max="{3}" step="{4}" class="" placeholder="" name="{5}"/>'.format(
                        input_id, ptype[1], ptype[2], ptype[3], ptype[4] , paras[0])

                except IndexError:
                    raise IOError("Are you sure you specified the default, min, max step of the number datatype ?? Or at least write number::::")
                print '</div>'

            elif ptype[0] == "text":
                print '<label class="control-label" for="{}">'.format(input_id)
                print paras[3] + ":"
                print '</label>'
                print '<div class="controls">'

                try:
                    print '<input id="{0}" type="text" value="{1}" pattern="{2}" class="" placeholder="" name="{3}"/>'.format(
                        input_id, ptype[1], ptype[2], paras[0])
                except IndexError:
                    raise IOError("Are you sure you specified the default and pattern of the text datatype ?? Or at least write text::")
                print '</div>'


            elif ptype[0] == "bool":
                print '<label class="checkbox">'
                print '<div class="controls">'
                print '<input type="checkbox" id="{0}" name="{1}">'.format(input_id, paras[0])
                print paras[3] + ":"
                print '</div>'
                print '</label>'

            elif ptype[0] == "radio":
                print paras[3] + ":"
                print '<div class="controls">'

                for choice in ptype[1:]:
                    print '<label class="radio">'
                    print '<input type="radio" name="{0}" value="{1}"/>'.format(
                        paras[0], choice)
                    print choice                                            
                    print '</label>'

                print '</div>'


            else:
                raise IOError("Datatype in column 4 not recognized. Should be either: 'number, text or bool'")

            print '</div>'
            print '</div>'

        print '</div> <!-- end of {} options -->'.format(prog)
        print '</div>'
        print '</div>'



    
#-------------------------------------------------------------------------------
if __name__ == "__main__":

    DATA = "data/test1.csv"
    print_soft_data(DATA)
    print_html(DATA)
