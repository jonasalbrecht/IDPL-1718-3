package myPlugin;

import com.intellij.openapi.project.Project;
import com.intellij.openapi.wm.ToolWindow;
import com.intellij.openapi.wm.ToolWindowFactory;
import com.intellij.ui.content.Content;
import com.intellij.ui.content.ContentFactory;
import org.jetbrains.annotations.NotNull;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.FocusEvent;
import java.awt.event.FocusListener;


public class MyToolWindow implements ToolWindowFactory {

    private JPanel panel;

    public MyToolWindow() {
    }

    @Override
    public void createToolWindowContent(@NotNull Project project, @NotNull ToolWindow toolWindow) {


       panel = new JPanel();
       panel.setSize(250, 250);

       JLabel lab= new JLabel();
       JTextField tf = new JTextField("");
       tf.setColumns(30);
       JButton but = new JButton("Find me Codeexamples!");
       but.setSize(50,15);
       tf.addFocusListener(new FocusListener() {
            public void focusGained(FocusEvent e) {
                tf.setText("");
            }
            public void focusLost(FocusEvent e) {
                // nothing
            }
        });
        but.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                buttonAction(evt);
            }
            private void buttonAction(ActionEvent evt) {
                lab.setText("You should use Google instead of asking me...");
            }
        });

        lab.setText("codeanswer here....");

        panel.add(tf);
        panel.add(but);
        panel.add(lab);


        final ContentFactory contentFactory = toolWindow.getContentManager().getFactory();
        final Content content = contentFactory.createContent(panel, "", true);
        toolWindow.getContentManager().addContent(content);
        toolWindow.setAutoHide(false);


    }
}
