package myPlugin;

import com.intellij.openapi.project.Project;
import com.intellij.openapi.wm.ToolWindow;
import com.intellij.openapi.wm.ToolWindowFactory;
import com.intellij.ui.content.Content;
import com.intellij.ui.content.ContentFactory;
import org.jetbrains.annotations.NotNull;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;


public class MyToolWindow implements ToolWindowFactory {

    private JPanel toplvlPanel;
    private JPanel panel;
    private JTextField tf;
    private ArrayList<String> resultsDemo = new ArrayList<String>();
    private ArrayList<JLabel> recom = new ArrayList<JLabel>();

    public MyToolWindow() {
        resultsDemo.add("First Result: Some nice stuff about arrays");
        resultsDemo.add("Second Result: Some nice stuff about lists");
        resultsDemo.add("Third Result: Some nice stuff about initializing");
        resultsDemo.add("Fourth Result: Some nice stuff about window-classes");
        resultsDemo.add("Fifth Result: Some nice stuff about allocating memory");
        resultsDemo.add("Sixth Result: Some nice stuff about deleting parts of an array");
        resultsDemo.add("Seventh Result: Some nice stuff about generating random numbers");
        resultsDemo.add("Eighth Result: Some nice stuff about parsing of strings");
        resultsDemo.add("Ninth Result: Some nice stuff about big integers");
        resultsDemo.add("Tenth Result: Some nice stuff about something completely different");
        resultsDemo.add("Eleventh Result: Some nice stuff about introduction to java");
    }

    @Override
    public void createToolWindowContent(@NotNull Project project, @NotNull ToolWindow toolWindow) {
        toplvlPanel = new JPanel(new BorderLayout());
        panel = new JPanel(new GridBagLayout());
        tf = new JTextField("");
        JButton but = new JButton("Correct Button, AMK!");
        GridBagConstraints c = new GridBagConstraints();

        toplvlPanel.add(panel, BorderLayout.NORTH);

        tf.setColumns(30);

        panel.setLayout(new GridBagLayout());
        c.fill = GridBagConstraints.HORIZONTAL;
        c.weightx = 0.75;
        c.gridx = 0;
        c.gridy = 0;
        c.anchor = GridBagConstraints.FIRST_LINE_START;
        panel.add(tf, c);
        c.weightx = 0.0;
        c.gridx = 1;
        //c.ipadx = 30;
        c.anchor = GridBagConstraints.FIRST_LINE_END;
        panel.add(but, c);

        tf.addFocusListener(new FocusListener() {
            public void focusGained(FocusEvent e) {
                tf.select(0, tf.getText().length());
            }
            public void focusLost(FocusEvent e) { }
        });

        tf.addKeyListener(new KeyListener() {
            @Override
            public void keyTyped(KeyEvent e) {
                // If ENTER is pressed
                if(e.getKeyChar() == '\n'){
                    showSolution(c);
                    System.out.println("ENTER PRESSED - SEARCH FOR RESULTS");
                }
            }
            @Override
            public void keyPressed(KeyEvent e) { }
            @Override
            public void keyReleased(KeyEvent e) { }
        });

        but.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                buttonAction(evt);
            }
            private void buttonAction(ActionEvent evt) {
                showSolution(c);
            }
        });

        // Adding this plugin to the environment
        final ContentFactory contentFactory = toolWindow.getContentManager().getFactory();
        final Content content = contentFactory.createContent(toplvlPanel, "", true);
        toolWindow.getContentManager().addContent(content);
        toolWindow.setAutoHide(false);
    }

    private void showSolution(GridBagConstraints c){
        if(tf.getText().equals("")){
            for(JLabel l : recom){
                panel.remove(l);
            }
            recom.clear();
        } else {
            c.weightx = 1;
            c.gridx = 0;
            c.gridwidth = 2;
            c.ipadx = 0;
            c.insets = new Insets(5,10,5,10);  // paddings
            c.anchor = GridBagConstraints.LINE_START;
            int i = 1;
            for (String s : resultsDemo) {
                JLabel lab = new JLabel();
                lab.setText(s);
                lab.addMouseListener(new MouseListener() {
                    @Override
                    public void mouseClicked(MouseEvent e) {
                        System.out.println("Mouse-Click-On-Label-Event executed:");
                        System.out.println(s);
                        System.out.println("My position in the recom-array: " + recom.indexOf(lab));
                    }
                    @Override
                    public void mousePressed(MouseEvent e) { }
                    @Override
                    public void mouseReleased(MouseEvent e) { }
                    @Override
                    public void mouseEntered(MouseEvent e) { }
                    @Override
                    public void mouseExited(MouseEvent e) { }
                });
                c.gridy = i;
                panel.add(lab, c);
                recom.add(lab);
                i++;
            }
        }
        panel.updateUI();
    }



}


//cikm string comparism