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


    - There is hierarchy in the event handler, and each handler 
     accept or propagate the event.


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

0. QMainWindow
    - Pre-made widget with featurefs for laout and additional components(toolbars, menus, ...).

1. QWidget







