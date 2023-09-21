Note Starts : 2023-09-18
------------------------------------------------------------------
* Static Objects - Objects for lendering, ...

1. QApplication - Specialized GUI Interface for QWidget
    - In PyQt API, it is used via QApplication.instance() 
     getter function.
    - Innitialization of QApplication is necessary 
     before any PyQt UI is created.

      => Due to the iinitialization of common data or cmd arg 
        related to system.
            * QWidget internally uses QApplication.

    - It deals with
        * Event handling(doubleClick, ...)
            : "exec()" method starts up the event handling loop.
        * argv(Default setting: topLevel, ...) or Style(palette,
         font....)
        * Management of Windows and modifcation of window setting.
        * Interface between event and QWidget, and QWidget 
         hiararchy management.
            => QApplication is the interface with the system,
              therefore need to be UNIQUE.

    
2. Event loop : 
    - System -> Event Queue  <=>  QApplication.exec()
                        => Event Handler(Accept? or Propagate?)
      * Note
       Exit of the window sends the "exit" event and 
      event loop is terminated.
            
    - Event loop collects events from the event queue and 
     feed to event handler.
        * Event handler is 

        * Terminology 
            Signal : Convey of Event to an event handler 
                of a widget.
            Slot   : Signal Receiver(Event Handler)
            Hook   : Register the slot to the widget.

        * Note, any function or method can be a slot.
        * Event loop checks the sequential events even in duration-check event.
            (The event is issued heurestically)
            ex) double click event == press -> release -> double click -> release
            ex) double click event == press -> move -> release -> double click -> release

        * Built-in handler does implicitly check the new state
            ex) 
            For double click event,
                press -> release -> double click -> release
            ,or  press -> release -> double click -> press -> release
            case 1 :
            def mouseDoubleClickEvent(self, e):
                print ("Double Click Issued")

            => After DoubleClick event, it could not check the press state
                (Logic follows : press -> release -> double click -> release)
                
            case 2 :
            def mouseDoubleClickEvent(self, e):
                print ("Double Click Issued")
                super().mouseDoubleClickEvent(e)

            => After DoubleClick event, it check the press event in super()
              and mousePressEvent(self, e) is issued.
                (Logic follows : press -> release -> double click -> ->press -> release)

            case 3 :
            def mouseDoubleClickEvent(self, e):
                super().mouseDoubleClickEvent(e)
                print ("Double Click Issued")

            => After DoubleClick event, it check the press event in super()
              and mousePressEvent(self, e) is issued. But, the handling(print) is
              executed after mousePressEvent is finished.
                (Logic follows : press -> release -> double click -> ->press -> release)



    - There is hierarchy in the event handler, and each handler 
     accept or propagate the event.


* Events
    - Event is a data structure, or object that QApplication created from the system interupt.
        ex) Event handler for mouse events (QMouseEvent)
        Handler : .mouseMoveEvent, .mousePressEvent, .mouseReleaseEvent, .mouseDoubleClickEvent
        Event : QMouseEvent
            * QMouseEvent Getter
            QMouseEvent.button()            Retrieve state of the current button event
            QMouseEvent.buttons()           Retrieve button state of the current mouse
            QMouseEvent.position()          Retrieve position state of the current mouse

            * QMouseEvent states            value (bit ptn) 
            Qt.MouseButton.NoButton         0 (000)         => Event not related to buttonpress
            Qt.MouseButton.LeftButton       1 (001)
            Qt.MouseButton.RightButton      2 (010)
            Qt.MouseButton.MiddleButton     4 (100)

        ex) QContextMenuEvent 
          => Event triggered when the window is right-clicked.
          => Event when the context menu is about to be shown.
            
        Handler : .contextMenuEvent
    
    - Layout forwarding (Widget Hierarchy)
        : The event is treated backward of Widget Hierarchy.(From childs to parent)
        => Upper widget of the hierarchy can be retreived with ".parent()".
        
        


* Action (QAction)


* Layout

* Widget Objects 
    - Objects that contains the User-Friendly rendering information
        and features.
    - Any widget can be windows.
    - Most widget has the corresponding built-in slots.
        * For example, the button is toggled when clicked.
            => event handling : Change toggle and how it looks 
    - Each widget can have several slots.

    - Widget is receive callbacks for event handling.
        => The state of widget or the data of event can be retrieved via
          getters of widget(built-in state) or callbacks.

    0. QWidget
        - Polymorphism Parent

    1. QMainWindow
        - Pre-made widget with features for layout and additional components(toolbars, menus, ...).

    2. QLabel
        - Text content, text style(font, alignment), Image
            * Text style is stored in "QWidget.font()" -> QFont structure
                => Always alter it, do not make new one.

        - QLabel also can show image. (QLabel as layout for QPixmap)
            ex) qlabel.setPixmap(QPixmap("otje.jpg"))
    3. QPixmap

    4. QCheckBox
        - Basically binary state 
            0 : Qt.CheckState.Unchecked
            2 : Qt.CheckState.Checked
        - Often tri state   (widget.setTristate(True))
            0 : Qt.CheckState.Unchecked
            1 : Qt.CheckState.PartiallyChecked
            2 : Qt.CheckState.Checked

    5. QComboBox
        - Adding items : widget.addItems(list)
        - Typical events :
            1. widget.currentIndexChanged   : When currently selected item is updated, give index.
            2. widget.currentTextChanged    : When the shown label is changed, give the label.
                => Two events are different when the comboBox is editable. (widget.setEditable(True))
                (2 are issued every typing of user , 1 is issued only when user entered new item)
                (Insert policy can be changable)
        - 

    6. QListWidget
        - Identical to QComboBox, but currentIndexChanged gives QListWidgetItem.
        - One line text UI.
        - Additional event handler should be noted.
            1. widget.sectionChanged    : When the dragged items is changed.
            2. widget.returnChanged     : When the "enter" key is enterred.
            3. widget.text_changed      : text is changed.
            4. widget.text_edited       : User starts to edit the text.(Time limit)
        - Inputmask (widget.setInputMask("000-0000-0000"))

    7. QSpinbox / QDoubleSpinbox
        - Number increasing with prefix, suffix, and step setting.
        - Range confine the values
        - It also acts with text input (widget.lineEdit())
            => Disable text input (widget.lineEdit().setReadOnly(True))

    8. QSlider
    9. QDial

    10. QTextEdit

    11. QMenu(Parent)








