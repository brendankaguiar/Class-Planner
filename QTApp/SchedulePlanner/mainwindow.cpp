#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->verticalFrame_12->setToolTip("HEWWO");
}

MainWindow::~MainWindow()
{
    delete ui;
}

//open file dialog to open a schedule file
void MainWindow::on_actionLoad_Schedule_triggered()
{
    QString fileName = QFileDialog::getOpenFileName(this, "Open schedule file", "C://");
    //fileName is the path to the file
    //then open the file and read data to load
}

