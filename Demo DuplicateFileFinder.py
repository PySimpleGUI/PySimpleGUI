import hashlib
import os
import win32clipboard
import PySimpleGUI as gg


# ====____====____==== FUNCTION DeDuplicate_folder(path) ====____====____==== #
# Function to de-duplicate the folder passed in                               #
# --------------------------------------------------------------------------- #
def FindDuplicatesFilesInFolder(path):
    shatab = []
    total = 0
    small = (1024)
    small_count, dup_count, error_count = 0,0,0
    pngdir = path
    if not os.path.exists(path):
        gg.MsgBox('De-Dupe', '** Folder doesn\'t exist***', path)
        return
    pngfiles = os.listdir(pngdir)
    total_files = len(pngfiles)
    not_cancelled = True
    for idx, f in enumerate(pngfiles):
        if not gg.EasyProgressMeter('Counting Duplicates', idx+1, total_files, 'Counting Duplicate Files'):
            break
        total += 1
        fname = os.path.join(pngdir, f)
        if os.path.isdir(fname):
            continue
        x = open(fname, "rb").read()

        m = hashlib.sha256()
        m.update(x)
        f_sha = m.digest()
        if f_sha in shatab:
            # os.remove(fname)
            dup_count += 1
            continue
        shatab.append(f_sha)

    msg = f'{total} Files processed\n'\
          f'{dup_count} Duplicates found\n'
    gg.MsgBox('Duplicate Finder Ended', msg)

# ====____====____==== Pseudo-MAIN program ====____====____==== #
# This is our main-alike piece of code                          #
#   + Starts up the GUI                                         #
#   + Gets values from GUI                                      #
#   + Runs DeDupe_folder based on GUI inputs                    #
# ------------------------------------------------------------- #
if __name__ == '__main__':

    source_folder = None
    rc, source_folder = gg.GetPathBox('DeDuplicate a Folder\'s image files', 'Enter path to folder you wish to find duplicates in')
    if rc is True and source_folder is not None:
        FindDuplicatesFilesInFolder(source_folder)
    else:
        gg.MsgBox('Cancelling', '*** Cancelling ***')
    exit(0)
