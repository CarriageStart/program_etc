
#include <cstdio>

class Base {
public:
    virtual void blink() {
        printf("Base blink is called.\n");
    }
    virtual void secretBlink() {
        printf("I'm am blink method which derived doesn't have.\n");
        printf("x is %d.\n", x);
    }
private:
    int x = 0;
};


class Derived: public Base {
public:
    Derived() {
        x = 3;
    }
    virtual void blink() {
        printf("Child blink is called.\n");
    }
    virtual void anotherBlink() {
        printf("I'm am blink method which Base doesn't have.\n");
        printf("x is %d.\n", x);
    }

private:
    int x = 0;

};

int main(int argc, char* args[]) {

    Derived* d = new Derived;
    d->blink();
    d->anotherBlink();
    d->secretBlink();

    Base* b = static_cast<Base*> (d);   // addr of vtable is changed to Parents.(Static casting)
    b->blink();
    b->secretBlink();
    // b->anotherBlink(); // This is not allowed. For this, dynamic_cast<Derived*> (b)->anotherBlink() is needed
    dynamic_cast<Derived*>(b)->anotherBlink(); 

    delete d;
    return 0;
}



