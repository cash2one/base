using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Web.Security;
using System.Windows.Forms;

namespace WechatURL
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                string ori = string.Empty;

                string msg = this.richTextBox1.Text.Trim();
                if (!string.IsNullOrEmpty(msg))
                    ori += "msg=" + msg + "&";
                string system = this.textBox1.Text.Trim();
                if (!string.IsNullOrEmpty(system))
                    ori += "system=" + system + "&";
                string dt = this.dateTimePicker1.Value.ToString("yyyyMMddHHmmss");
                if (!string.IsNullOrEmpty(system))
                    ori += "ts=" + dt + "&";
                string user = this.textBox2.Text.Trim();
                if (!string.IsNullOrEmpty(system))
                    ori += "user=" + user + "&";
                ori += "key=8934e7d15453e97507ef794cf7b0519d";
                string enc = FormsAuthentication.HashPasswordForStoringInConfigFile(ori, "MD5");
                this.textBox3.Text = string.Format("http://www.subinwechat.com/p/ParkingWechatAuthorize.html?msg={0}&system={1}&ts={2}&user={3}&sign={4}&syscolor={5}&strict={6}&scope={7}",
                    msg, system, dt, user, enc, this.textBox4.Text.Trim(), this.comboBox1.Text.Trim(), this.comboBox2.Text.Trim());
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void textBox4_Click(object sender, EventArgs e)
        {

        }
    }
}
