#include "dynamicclass.h"
#include "ui_mainwindow.h"

//code modified from https://github.com/VelazcoJD/QtDynamicWidgets

DynamicClass::DynamicClass(QWidget *parent) : QMainWindow(parent)
{

}

DynamicClass::~DynamicClass()
{

}

void DynamicClass::onAddClass()
{
    QHBoxLayout* layout = qobject_cast<QHBoxLayout*>(ui->HoldingFrame->layout()); //code modified from https://github.com/VelazcoJD/QtDynamicWidgets

}

void DynamicClass::onRemoveClass()
{

}
