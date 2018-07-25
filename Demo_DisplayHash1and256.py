#!Python 3
import hashlib
import PySimpleGUI as SG

 #########################################################################
# DisplayHash                                                            #
#   A PySimpleGUI demo app that displays SHA1 hash for user browsed file #
#   Useful and a recipe for GUI success                                  #
 #########################################################################

# ====____====____==== FUNCTION compute_hash_for_file(filename) ====____====____==== #
# Reads a file, computes the Hash                                                    #
# ---------------------------------------------------------------------------------- #
def compute_sha1_hash_for_file(filename):
    try:
        x = open(filename, "rb").read()
    except:
        return 0

    m = hashlib.sha1()
    m.update(x)
    f_sha = m.hexdigest()

    return f_sha


# ====____====____==== FUNCTION compute_hash_for_file(filename) ====____====____==== #
# Reads a file, computes the Hash                                                    #
# ---------------------------------------------------------------------------------- #
def compute_sha256_hash_for_file(filename):
    try:
        f = open(filename, "rb")
        x = f.read()
    except:
        return 0

    m = hashlib.sha256()
    m.update(x)
    f_sha = m.hexdigest()

    return f_sha


 # ====____====____==== Uses A GooeyGUI GUI ====____====____== #
#  Get the filename, display the hash, dirt simple all around   #
 # ----------------------------------------------------------- #

# ---------------------------------------------------------------------- #
#   Compute and display SHA1 hash                                        #
#   Builds and displays the form using the most basic building blocks    #
# ---------------------------------------------------------------------- #
def HashManuallyBuiltGUI():
    # -------  Form design ------- #
    with SG.FlexForm('SHA-1 & 256 Hash', auto_size_text=True) as form:
        form_rows = [[SG.Text('SHA-1 and SHA-256 Hashes for the file')],
                     [SG.InputText(), SG.FileBrowse()],
                     [SG.Submit(), SG.Cancel()]]
        (button, (source_filename, )) = form.LayoutAndShow(form_rows)

    if button == 'Submit':
        if source_filename != '':
            hash_sha1 = compute_sha1_hash_for_file(source_filename).upper()
            hash_sha256 = compute_sha256_hash_for_file(source_filename).upper()
            SG.MsgBox( 'Display A Hash in PySimpleGUI', 'The SHA-1 Hash for the file\n', source_filename, hash_sha1, 'SHA-256 is', hash_sha256, line_width=75)
        else: SG.MsgBoxError('Display A Hash in PySimpleGUI', 'Illegal filename')
    else:
        SG.MsgBoxError('Display A Hash in PySimpleGUI', '* Cancelled *')

def HashManuallyBuiltGUINonContext():
    # -------  Form design ------- #
    form = SG.FlexForm('SHA-1 & 256 Hash', auto_size_text=True)
    form_rows = [[SG.Text('SHA-1 and SHA-256 Hashes for the file')],
                     [SG.InputText(), SG.FileBrowse()],
                     [SG.Submit(), SG.Cancel()]]
    button, (source_filename, ) = form.LayoutAndShow(form_rows)

    if button == 'Submit':
        if source_filename != '':
            hash_sha1 = compute_sha1_hash_for_file(source_filename).upper()
            hash_sha256 = compute_sha256_hash_for_file(source_filename).upper()
            SG.MsgBox( 'Display A Hash in PySimpleGUI', 'The SHA-1 Hash for the file\n', source_filename, hash_sha1, 'SHA-256 is', hash_sha256, line_width=75)
        else: SG.MsgBoxError('Display A Hash in PySimpleGUI', 'Illegal filename')
    else:
        SG.MsgBoxError('Display A Hash in PySimpleGUI', '* Cancelled *')




# ---------------------------------------------------------------------- #
#   Compute and display SHA1 hash                                        #
#   This one cheats and uses the higher-level Get A File pre-made func   #
#   Hey, it's a really common operation so why not?                      #
# ---------------------------------------------------------------------- #
def HashMostCompactGUI():
    # -------  INPUT GUI portion  ------- #

    rc, source_filename = SG.GetFileBox('Display A Hash Using PySimpleGUI',
                                  'Display a Hash code for file of your choice')

    # -------  OUTPUT GUI results portion  ------- #
    if rc == True:
        hash = compute_sha1_hash_for_file(source_filename)
        SG.MsgBox('Display Hash - Compact GUI', 'The SHA-1 Hash for the file\n', source_filename, hash)
    else:
        SG.MsgBox('Display Hash - Compact GUI', '* Cancelled *')


# ---------------------------------------------------------------------- #
#  Our main calls two GUIs that act identically but use different calls  #
# ---------------------------------------------------------------------- #
def main():
    HashManuallyBuiltGUINonContext()
    HashMostCompactGUI()


# ====____====____==== Pseudo-MAIN program ====____====____==== #
# This is our main-alike piece of code                          #
#   + Starts up the GUI                                         #
#   + Gets values from GUI                                      #
#   + Runs DeDupe_folder based on GUI inputs                    #
# ------------------------------------------------------------- #
if __name__ == '__main__':
    main()
