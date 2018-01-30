package myPlugin;

import com.intellij.openapi.project.Project;
import com.intellij.openapi.wm.ToolWindow;
import com.intellij.openapi.wm.ToolWindowFactory;
import com.intellij.ui.content.Content;
import com.intellij.ui.content.ContentFactory;
import com.wcohen.ss.SmithWaterman;
import org.jetbrains.annotations.NotNull;

import javax.swing.*;
import javax.xml.crypto.Data;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;


public class MyToolWindow implements ToolWindowFactory {

    private JPanel toplvlPanel;
    private JPanel panel;
    private JTextField tf;
    private ArrayList<JLabel> recom = new ArrayList<JLabel>();

    private ArrayList<DataPair> dataPairs = new ArrayList<>();
    private SmithWaterman sm = new SmithWaterman();

    private ArrayList<DataPair> getTopFive(String text) {
        ArrayList<DataPair> topFive = new ArrayList<>();
        for(DataPair dp : dataPairs){
            setSM_score(text, dp);
            addToTopTive(dp, topFive);
        }
        return topFive;
    }

    private double setSM_score(String source, DataPair dp){
        dp.setScore(sm.score(source, dp.getDescription()));
        return dp.getScore();
    }

    private void addToTopTive(DataPair dp, ArrayList<DataPair> targetArray){
        if(targetArray.isEmpty()){
            targetArray.add(dp);
        }
        for(int i = 0; i < targetArray.size(); i++){
            if(dp.getScore() >= targetArray.get(i).getScore()){
                targetArray.add(i, dp);
                while(targetArray.size() > 5){
                    targetArray.remove(5);
                }
                return;
            }
        }
    }

    public MyToolWindow() {
        dataPairs.add(new DataPair("matrix.I", "Returns the (multiplicative) inverse of invertible self."));
        dataPairs.add(new DataPair("matrix.A","Return self as an ndarray object."));
        dataPairs.add(new DataPair("matrix","Returns a matrix from an array-like object, or from a string of data."));
        dataPairs.add(new DataPair("asmatrix(data[, dtype])","Interpret the input as a matrix."));
        dataPairs.add(new DataPair("bmat(obj[, ldict, gdict])","Build a matrix object from a string, nested sequence, or array."));
        dataPairs.add(new DataPair("memmap","Create a memory-map to an array stored in a binary file on disk."));
        dataPairs.add(new DataPair("memmap.flush()","Write any changes in the array to the file on disk."));
        dataPairs.add(new DataPair("chararray","Provides a convenient view on arrays of string and unicode values."));
        dataPairs.add(new DataPair("core.defchararray.array(obj[, itemsize, ...])","Create a chararray"));
        dataPairs.add(new DataPair("recarray","Construct an ndarray that allows field access using attributes."));
    }

    @Override
    public void createToolWindowContent(@NotNull Project project, @NotNull ToolWindow toolWindow) {
        toplvlPanel = new JPanel(new BorderLayout());
        panel = new JPanel(new GridBagLayout());
        tf = new JTextField("");
        JButton but = new JButton("Search");
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
        String evalString = tf.getText();
        for(JLabel l : recom){
            panel.remove(l);
        }
        recom.clear();
        if(evalString.equals("")){
            // Do nothing
        } else {
            c.weightx = 1;
            c.gridx = 0;
            c.gridwidth = 2;
            c.ipadx = 0;
            c.insets = new Insets(5,10,5,10);  // paddings
            c.anchor = GridBagConstraints.LINE_START;
            ArrayList<DataPair> results = getTopFive(evalString);
            int i = 1;
            for (DataPair dp : results) {
                JLabel lab = new JLabel();
                lab.setText(dp.getDescription());
                lab.addMouseListener(new MouseListener() {
                    @Override
                    public void mouseClicked(MouseEvent e) {
                        System.out.println("Mouse-Click-On-Label-Event executed:");
                        System.out.println(dp.getScore());
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