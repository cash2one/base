using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Windows.Forms;

namespace QRCode
{
    public partial class Form1 : Form
    {
        //密钥"voncytel"
        static byte[] Key = new byte[] { 0x76, 0x6f, 0x6e, 0x63, 0x79, 0x74, 0x65, 0x6c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };
        //向量
        static byte[] VI = new byte[] { 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };
        //二维码扫出来的加密hex字符串
        static byte[] data = new byte[] { 0x8C, 0x1A, 0xF0, 0x50, 0x8C, 0x1C, 0x29, 0xBE, 0xED, 0xEE, 0x4E, 0xF9, 0x15, 0x51, 0x3B, 0xF8, 0xFD, 0x09, 0x3D, 0x9C, 0xB4, 0x91, 0x7E, 0x12, 0x16, 0x78, 0x18, 0x5F, 0xC9, 0x0F, 0x95, 0xAC, 0xA2, 0x70, 0xA7, 0x55, 0x38, 0x9B, 0xAC, 0xD2, 0xA2, 0xC7, 0xBC, 0x35, 0xE0, 0x21, 0x7F, 0x2B };


        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                this.richTextBox2.Text = Encrypt(this.richTextBox1.Text.Trim());
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            try
            {
                this.richTextBox1.Text = AESDecrypt(strToToHexByte(this.richTextBox2.Text.Trim())).Replace('\0', ' ').Trim();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        /// <summary>
        /// 字符串转16进制字节数组
        /// </summary>
        /// <param name="hexString"></param>
        /// <returns></returns>
        private static byte[] strToToHexByte(string hexString)
        {
            hexString = hexString.Replace(" ", "");
            if ((hexString.Length % 2) != 0)
                hexString += " ";
            byte[] returnBytes = new byte[hexString.Length / 2];
            for (int i = 0; i < returnBytes.Length; i++)
                returnBytes[i] = Convert.ToByte(hexString.Substring(i * 2, 2), 16);
            return returnBytes;
        }

        public static string AESDecrypt(byte[] data)
        {
            RijndaelManaged rijndaelCipher = new RijndaelManaged();
            rijndaelCipher.Mode = CipherMode.CBC;
            rijndaelCipher.Padding = PaddingMode.Zeros;

            rijndaelCipher.Key = Key;
            rijndaelCipher.IV = VI;

            ICryptoTransform transform = rijndaelCipher.CreateDecryptor();

            byte[] plainText = transform.TransformFinalBlock(data, 0, data.Length);

            return Encoding.UTF8.GetString(plainText);

        }

        ///// <summary>
        ///// AES解密
        ///// </summary>
        ///// <param name="text"></param>
        ///// <param name="password"></param>
        ///// <param name="iv"></param>
        ///// <returns></returns>
        public static string AESDecrypt()
        {
            RijndaelManaged rijndaelCipher = new RijndaelManaged();
            rijndaelCipher.Mode = CipherMode.CBC;
            rijndaelCipher.Padding = PaddingMode.Zeros;

            rijndaelCipher.Key = Key;
            rijndaelCipher.IV = VI;

            ICryptoTransform transform = rijndaelCipher.CreateDecryptor();

            byte[] plainText = transform.TransformFinalBlock(data, 0, data.Length);

            return Encoding.UTF8.GetString(plainText);

        }

        ///// <summary>
        ///// AES加密
        ///// </summary>
        ///// <param name="toEncrypt"></param>
        ///// <returns></returns>
        public static string Encrypt(string toEncrypt)
        {
            byte[] toEncryptArray = UTF8Encoding.UTF8.GetBytes(toEncrypt);

            RijndaelManaged rDel = new RijndaelManaged();
            rDel.Key = Key;
            rDel.IV = VI;
            rDel.Mode = CipherMode.CBC;
            rDel.Padding = PaddingMode.Zeros;

            ICryptoTransform cTransform = rDel.CreateEncryptor();
            byte[] resultArray = cTransform.TransformFinalBlock(toEncryptArray, 0, toEncryptArray.Length);
            return ByteToString(resultArray);
        }

        ///// <summary>
        /////格式化输出十六进制字符串
        ///// </summary>
        ///// <param name="InBytes"></param>
        ///// <returns></returns>
        public static string ByteToString(byte[] InBytes)
        {
            string StringOut = string.Empty;
            foreach (byte InByte in InBytes)
            {
                string msg = String.Format("{0:X2} ", InByte).Trim();
                StringOut = StringOut + msg;
            }
            return StringOut;
        }
    }
}
