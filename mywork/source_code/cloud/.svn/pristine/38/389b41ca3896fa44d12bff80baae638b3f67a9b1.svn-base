
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using Cytel.Cloud.DataUPloadService.VBM;
using Cytel.Cloud.DataUPloadService.ListenerIF;

namespace Cytel.Cloud.DataUploadService.Demo
{
    public partial class Form1 : Form
    {
      

        public Form1()
        {
            InitializeComponent();
          
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            IListener l = new VBMListener();
            l.Start();
        }
    }
}
