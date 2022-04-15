#ifndef DYNAMICCLASS_H
#define DYNAMICCLASS_H

#include <QMainWindow>
#include <QWidget>
#include <mainwindow.h>


class DynamicClass : public QMainWindow
{
    Q_OBJECT
private:
    Ui::MainWindow *ui;
public:

    DynamicClass(QWidget *parent = nullptr);

    ~DynamicClass();

    void onAddClass();

    void onRemoveClass();

};

#endif // DYNAMICCLASS_H
