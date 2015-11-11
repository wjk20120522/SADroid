// package com.utils;

import java.io.File;
import java.io.IOException;
import java.lang.System;

public class FileAnalysis implements Runnable{

    private String input_apkfile;
    private String output_apkfile;

    FileAnalysis(String input_apkfile, String output_apkfile) {
        this.input_apkfile = input_apkfile;
        this.output_apkfile = output_apkfile;
    }

    @Override
    public void run() {

        String[] cmd = new String[6];

        cmd[0] = "python";
        cmd[1] = "/Users/wjk/Desktop/SADroid/apk_info.py";    // 静态分析脚本位置
        cmd[2] = "-i";
        cmd[3] = input_apkfile;            // 输入的apk文件位置
        cmd[4] = "-o";
        cmd[5] = output_apkfile;         // 输出的文件位置

        try {
            Process proc = Runtime.getRuntime().exec(cmd);
            proc.waitFor();
        } catch (InterruptedException | IOException e) {
            e.printStackTrace();
        }
    }

}
