using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Web.Security;
using System.Windows.Forms;

namespace CouponURL
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
                string guid = Guid.NewGuid().ToString("N");
                ori += "id=" + guid + "&";

                string price = this.textBox4.Text.Trim();
                if (!string.IsNullOrEmpty(price))
                    ori += "price=" + price + "&";


                string seller = this.textBox2.Text.Trim();
                if (!string.IsNullOrEmpty(seller))
                    ori += "seller=" + seller + "&";


                string msg = this.richTextBox1.Text.Trim();
                if (!string.IsNullOrEmpty(msg))
                    ori += "msg=" + msg + "&";

                string system = this.textBox1.Text.Trim();
                if (!string.IsNullOrEmpty(system))
                    ori += "system=" + system + "&";

                string dt = this.dateTimePicker1.Value.ToString("yyyyMMddHHmmss");
                if (!string.IsNullOrEmpty(system))
                    ori += "time=" + dt + "&";
               
                ori += "key=8934e7d15453e97507ef794cf7b0519d";
                string enc = FormsAuthentication.HashPasswordForStoringInConfigFile(ori, "MD5");
                this.textBox3.Text = string.Format("{0}?system={1}&seller={2}&time={3}&price={4}&id={5}&msg={6}&sign={7}",
                    this.textBox5.Text.Trim(), system, seller, dt, price, guid, msg, enc);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
    }
}
