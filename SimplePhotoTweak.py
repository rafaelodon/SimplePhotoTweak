#!/usr/bin/python

# Simple Photo Tweak
#
# author: Rafael Odon
#

import gtk

class SimplePhotoTweak(gtk.Window):

    def __init__(self):
        super(SimplePhotoTweak, self).__init__()

        self.image = gtk.Image();

        self.configWindow();

        mb = self.generateMenu();
        imageArea = self.generateImageArea();

        vbox = gtk.VBox(False, 2);        
        vbox.pack_start(mb, False, False, 0);        
        vbox.pack_start(imageArea, True, True, 0);

        self.add(vbox)

        self.connect("destroy", gtk.main_quit)
        self.show_all()
    
    def configWindow(self):        
        screen = gtk.Window().get_screen()

        self.set_title("Simple Photo Tweak")
        self.set_size_request(int(screen.get_width() * 0.8), int(screen.get_height() * 0.8))        
        self.set_position(gtk.WIN_POS_CENTER)

    def generateMenu(self):
        mb = gtk.MenuBar();

        filemenu = gtk.Menu();        
        filem = gtk.MenuItem("File");
        filem.set_submenu(filemenu);        

        openmenu = gtk.MenuItem("Open File...");
        openmenu.connect("activate", self.selectFile);
        filemenu.append(openmenu);

        filemenu.append(gtk.SeparatorMenuItem());

        exit = gtk.MenuItem("Quit");
        exit.connect("activate", gtk.main_quit);
        filemenu.append(exit);

        mb.append(filem);

        return mb;

    def generateImageArea(self):        

        imageArea = gtk.ScrolledWindow();        
        imageArea.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)

        imageArea.add_with_viewport(self.image);
        imageArea.show();

        return imageArea;

    def selectFile(self, widget):

        dialog = gtk.FileChooserDialog("Open..", None, gtk.FILE_CHOOSER_ACTION_OPEN,
            (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OPEN, gtk.RESPONSE_OK));

        dialog.set_default_response(gtk.RESPONSE_OK);
        
        filter = gtk.FileFilter();
        filter.set_name("Common image files (*.png, *.jpg, *.jpeg, *.gif)");
        filter.add_mime_type("image/png");
        filter.add_mime_type("image/jpeg");
        filter.add_mime_type("image/gif");
        filter.add_pattern("*.png");
        filter.add_pattern("*.jpg");
        filter.add_pattern("*.jpeg");
        filter.add_pattern("*.gif");   
        dialog.add_filter(filter);

        response = dialog.run();
        
        if response == gtk.RESPONSE_OK:
            self.image.set_from_file(dialog.get_filename());
            self.image.show();
        
        dialog.destroy();
            
if __name__ == "__main__":
    SimplePhotoTweak();
    gtk.main();