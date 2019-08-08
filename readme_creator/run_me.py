from make_real_readme import main

########################################################################
#                              __ _            _                       #
#                             / _(_)          | |                      #
#    __   __   ___ ___  _ __ | |_ _  __ _     | |__   ___ _ __ ___     #
#    \ \ / /  / __/ _ \| '_ \|  _| |/ _` |    | '_ \ / _ \ '__/ _ \    #
#     \ V /  | (_| (_) | | | | | | | (_| |    | | | |  __/ | |  __/    #
#      \_/    \___\___/|_| |_|_| |_|\__, |    |_| |_|\___|_|  \___|    #
#                                    __/ |                             #
#                                   |___/                              #
########################################################################
OUTPUT_FILENAME = 'readme.md'

##-#-#-# ##-#-#-#
# Pre-process logic
##-#-#-# ##-#-#-#

line_break = '<br>'
# line_break can be:
# - '<br>'
# - ' \n '

method = 'with logs'
# method can be:
# - 'simple, no log'
# - 'with logs'


##-#-#-# ##-#-#-#
# Post-process logic
##-#-#-# ##-#-#-#
enable_popup = True
insert_md_section_for__class_methods = False
remove_repeated_sections_classmethods = False



##############
#     __     #
#    /_ |    #
#     | |    #
#     | |    #
#     | |    #
#     |_|    #
##############
if method == 'simple, no log':
    main(logger=None,
         insert_md_section_for__class_methods=insert_md_section_for__class_methods,
         remove_repeated_sections_classmethods=remove_repeated_sections_classmethods,
         files_to_include=[0, 1, 2, 3],
         output_name=OUTPUT_FILENAME,
         delete_html_comments=True)

################
#     ___      #
#    |__ \     #
#       ) |    #
#      / /     #
#     / /_     #
#    |____|    #
################
if method == 'with logs':

    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    my_file = logging.FileHandler('usage.log.txt', mode='w')
    my_file.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s>%(levelname)s: %(message)s')
    my_file.setFormatter(formatter)
    logger.addHandler(my_file)
    logger.info('STARTING')
    
    main(logger=logger,
         insert_md_section_for__class_methods=insert_md_section_for__class_methods,
         remove_repeated_sections_classmethods=remove_repeated_sections_classmethods,
         files_to_include=[0, 1, 2, 3],
         output_name=OUTPUT_FILENAME,
         delete_html_comments=True)

########################################
#     _____                            #
#    |  __ \                           #
#    | |__) |__  _ __  _   _ _ __      #
#    |  ___/ _ \| '_ \| | | | '_ \     #
#    | |  | (_) | |_) | |_| | |_) |    #
#    |_|   \___/| .__/ \__,_| .__/     #
#               | |         | |        #
#               |_|         |_|        #
########################################
if enable_popup:
    import PySimpleGUI as sg
    lines = open('usage.log.txt', mode='r').readlines()
    sg.PopupScrolled('Completed making {}'.format(OUTPUT_FILENAME), ''.join(lines), size=(80,50))


