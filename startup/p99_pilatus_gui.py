import os
import sys
sys.path.append('/home/xf08id/Repos/xpilatus/')
if not os.environ.get('AZURE_TESTING'):
    from pilatus_tools.widgets.widget_pilatus import UIPilatusMonitor
    pilatus_gui = UIPilatusMonitor(detector_dict=detector_dictionary, hhm=hhm)
    pilatus_gui.show()
    # print('test')