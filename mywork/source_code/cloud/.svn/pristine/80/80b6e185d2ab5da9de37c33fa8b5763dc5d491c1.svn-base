using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Cytel.Cloud.DataUPloadService.ListenerIF;
using Cytel.Common.Log;
using System.Net.Sockets;
using System.Net;
using System.Configuration;
using System.Threading;
using Cytel.Cloud.DataUPloadService.Model;
using Cytel.Cloud.DataInteractiveService.Model;
using System.Xml;
using Cytel.Common.Json;
using System.Security.Cryptography;
using Cytel.Cloud.DataUPloadService.Interactive;

namespace Cytel.Cloud.DataUPloadService.VBM
{
    public class VBMListener : IListener
    {

        #region IListener 成员
        private Socket VBMSocket = null;
        private ManualResetEvent VBMDone = new ManualResetEvent(false);
        private int BufferSize = 1024;
        private byte[] Buffer = new byte[1024];
        private bool VBMConnect = true;
        //t1监听服务器连接情况
        System.Timers.Timer t1 = new System.Timers.Timer(10000);
        private static MSpaceInfo sp =null;
        private static ConfigInfo configinfo = new ConfigInfo();//配置文件信息
        static object OBJ = new object();
        private void theout(object source, System.Timers.ElapsedEventArgs e)
        {
            InItConnectVBMServer();
        }
    
        public void Start()
        {           
            LogWrapper.WriteInfo("启动中...");
            t1.Elapsed += new System.Timers.ElapsedEventHandler(theout); //timer绑定事件
            //初始化sp
            sp = GetSpaceInfo();
            //获取配置文件信息
            GetAppSetting();
            //连接服务器
            InItConnectVBMServer();
            
        }
        private void GetAppSetting()
        {
            try
            {
                configinfo.ListenPort = Convert.ToInt32(ConfigurationSettings.AppSettings["ListenPort"]);
                configinfo.VBMServer = ConfigurationSettings.AppSettings["MC3HostName"];
                configinfo.ParkID = ConfigurationSettings.AppSettings["Park_ID"];
                configinfo.POSTURL = ConfigurationSettings.AppSettings["PostURL"];
                configinfo.Serect = ConfigurationSettings.AppSettings["Serect"];
            }
            catch (Exception ec)
            {
                LogWrapper.WriteError(ec.ToString());
            }
        }
        private void InItConnectVBMServer()//初始化操作
        {
            if (VBMSocket != null)
                VBMSocket.Close();
            try
            {
                VBMSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
                IPEndPoint VBMIP = new IPEndPoint(System.Net.IPAddress.Parse(configinfo.VBMServer), configinfo.ListenPort);
                VBMDone.Reset();
                VBMSocket.BeginConnect(VBMIP, VBMconnCallBack, VBMSocket);
                if (VBMDone.WaitOne(3000, false))//VBM连接服务器成功
                {
                    VBMSocket.BeginReceive(Buffer, 0, BufferSize, 0, new AsyncCallback(ReadaVBMCallBack), VBMSocket);//开始一个异步操作来接受一个传入的连接尝试（抛出异常未连接成功）  
                    LogWrapper.WriteInfo("启动成功，开始监听");
                    VBMConnect = true;
                    t1.Stop();
                }
                else
                {
                    VBMSocket.Close();
                    if (VBMConnect)
                    {
                        LogWrapper.WriteInfo("服务器连接失败，启动失败");
                        VBMConnect = false;
                    }
                    t1.Start();
                }
            }
            catch (Exception ex)
            {
                if (VBMConnect)
                {
                    LogWrapper.WriteError(ex.ToString());
                    VBMConnect = false;
                }
                t1.Start();
            }
        }
        private void VBMconnCallBack(IAsyncResult ar)
        {
            VBMDone.Set();
        }
        private void ReadaVBMCallBack(IAsyncResult ar)
        {
            try
            {
                Socket handler = (Socket)ar.AsyncState;
                int bytesRead = handler.EndReceive(ar); //结束挂起的异步读取,返回接收到的字节数。              
                if (bytesRead > 0)//
                {
                    String content = Encoding.ASCII.GetString(Buffer, 0, bytesRead);
                    handler.BeginReceive(Buffer, 0, BufferSize, 0, new AsyncCallback(ReadaVBMCallBack), handler);//开始一个异步操作来接受一个传入的连接尝试 
                    LogWrapper.WriteInfo("Recv Info from VBM:" + BitConverter.ToString(Encoding.ASCII.GetBytes(content)).Replace("-", " "));
                    StartDispatch(content);
                }
                else//服务器端中断客户端会接收到0个字节长度报文
                {
                    LogWrapper.WriteInfo("服务器断开连接");
                    VBMConnect = false;
                    t1.Start();
                }
            }
            catch (Exception ex)
            {
               
                LogWrapper.WriteError(ex.ToString());
            }
        }
        private void StartDispatch(string revinfo)
        {
            lock (OBJ)//同步
            {
                string[] ArrInfo = revinfo.Split('.');
                if (ArrInfo.Length == 4)
                {
                    try
                    {
                        string DeviceType = revinfo.Substring(3, 1);//设备类型
                        int DeviceNo = Convert.ToInt32(revinfo.Substring(5, 2));//设备编号
                        string DeviceName = DeviceType + DeviceNo.ToString();//设备名称
                        string CardNo = ArrInfo[1].Substring(0, 12);//获取12位卡号
                        //报文中获取时间
                        string CreateTime = string.Empty;
                        if (ArrInfo[2].Trim().Length == 12)
                        {
                            CreateTime = DateTime.Now.ToString("yyyyMMddHHmmss").Substring(0, 2) + ArrInfo[2];
                            CreateTime = DateTime.ParseExact(CreateTime, "yyyyMMddHHmmss", null).ToString("yyyy-MM-dd hh:mm:ss");
                        }
                        else
                        {
                            CreateTime = DateTime.Now.ToString("yyyyMMddHHmmss").Substring(0, 2) + ArrInfo[2].Substring(0, 10) + DateTime.Now.ToString("yyMMddHHmmss").Substring(10, 2);
                            CreateTime = DateTime.ParseExact(CreateTime, "yyyyMMddHHmmss", null).ToString("yyyy-MM-dd hh:mm:ss");
                        }
                        string CarType = ArrInfo[1].Substring(ArrInfo[1].Length - 2, 2);//获取车卡类别（时租00  月租30）
                        if (DeviceType.Equals("E"))//车辆进入剩余车位数-1
                        {

                            MEnterRequest MEnter = new MEnterRequest();
                            MEnter.ParkId = configinfo.ParkID;
                            MEnter.GateName = DeviceName;
                            MEnter.ETime = DateTime.ParseExact(CreateTime, "yyyy-MM-dd HH:mm:ss", null);
                            MEnter.CardNo = CardNo;
                            switch (CarType)
                            {
                                case "00"://时租车辆进场
                                    MEnter.EType = MCarType.Temp;
                                    LogWrapper.WriteInfo("the temp car enter:the old Ftemp Number is" + sp.FTemp.ToString());
                                    sp.FTemp = (sp.FTemp - 1) > 0 ? (sp.FTemp - 1) : 0;
                                    UpdataParkingInfo("FTemp", sp.FTemp.ToString());
                                    LogWrapper.WriteInfo("the temp car enter:the new Ftemp Number is" + sp.FTemp.ToString());
                                    break;
                                case "30"://月租车辆进入场
                                    MEnter.EType = MCarType.FullDayMonthly;
                                    LogWrapper.WriteInfo("the Month car enter:the old FMonthly Number is" + sp.FMonthly.ToString());
                                    sp.FMonthly = (sp.TMonthly - 1) > 0 ? (sp.TMonthly - 1) : 0;
                                    UpdataParkingInfo("TMonthly", sp.TMonthly.ToString());
                                    LogWrapper.WriteInfo("the Month car enter:the new FMonthly Number is" + sp.FMonthly.ToString());
                                    break;
                                default:
                                    break;
                            }
                            sp.FSpace = sp.FTemp + sp.FMonthly;
                            MEnter.SpaceInfo = sp;
                            string EnterStr = JsonConvert.SerializeObject(MEnter);
                            MRequestBase mrequest = new MRequestBase();
                            mrequest.User = "subin";
                            mrequest.Data = EnterStr;
                            mrequest.Method = "enter";
                            mrequest.Version = "1.0";
                            mrequest.RequestToken = Guid.NewGuid().ToString();
                            mrequest.TimeStamp = GetTimeStamp();
                            mrequest = ReturnMRequestBase(mrequest);
                            string RequestJson = JsonConvert.SerializeObject(mrequest);
                            LogWrapper.WriteInfo("Send enter Json:" + RequestJson);
                            string result = MessageUploader.PostJson(RequestJson, configinfo.POSTURL);
                            if (!string.IsNullOrEmpty(result))
                            {
                                try
                                {
                                    result = result.Replace(@"\", "");
                                    int begin = result.IndexOf('{');
                                    int end = result.LastIndexOf('}');
                                    result = result.Substring(begin, end);
                                    MResponseBase Rresult = JsonConvert.DeserializeObject<MResponseBase>(result);
                                    if (Rresult.Success == true)
                                    {
                                        LogWrapper.WriteInfo("Send exit Json Success ");
                                    }
                                    else
                                    {
                                        LogWrapper.WriteInfo("Send exit Json fault " );
                                    }
                                }
                                catch (Exception ex)
                                {
                                    LogWrapper.WriteError(ex.ToString());
                                }
                            }
                            else
                            {
                                LogWrapper.WriteInfo("Send exit Json fault " );
                            }
                            //post EN
                        }
                        else if (DeviceType.Equals("A") || DeviceType.Equals("O"))//离场剩余车位数+1
                        {
                            MExitRequest Ex = new MExitRequest();
                            Ex.ParkId = configinfo.ParkID;
                            Ex.GateName = DeviceName;
                            Ex.KTime = DateTime.ParseExact(CreateTime, "yyyy-MM-dd HH:mm:ss", null);
                            Ex.CardNo = CardNo;
                            switch (CarType)
                            {
                                case "00"://时租车辆离场
                                    Ex.KType = MCarType.Temp;
                                    LogWrapper.WriteInfo("the temp car exit:the old Ftemp Number is" + sp.FTemp.ToString());
                                    sp.FTemp = (sp.FTemp + 1) > sp.TTemp ? sp.TTemp : (sp.FTemp + 1);
                                    //修改配置文件剩余时租车
                                    UpdataParkingInfo("FTemp", sp.FTemp.ToString());
                                    LogWrapper.WriteInfo("the temp car exit:the new Ftemp Number is" + sp.FTemp.ToString());
                                    break;
                                case "30"://月租车辆离场
                                    Ex.KType = MCarType.FullDayMonthly;
                                    LogWrapper.WriteInfo("the Month car exit:the old FMonthly Number is" + sp.FMonthly.ToString());
                                    sp.FMonthly = (sp.FMonthly + 1) > sp.TMonthly ? sp.TMonthly : (sp.FMonthly + 1);
                                    //修改配置文件
                                    UpdataParkingInfo("TMonthly", sp.TMonthly.ToString());
                                    LogWrapper.WriteInfo("the Month car exit:the new FMonthly Number is" + sp.FMonthly.ToString());
                                    break;
                                default:
                                    break;
                            }
                            sp.FSpace = sp.FTemp + sp.FMonthly;
                            Ex.SpaceInfo = sp;
                            string ExitStr = JsonConvert.SerializeObject(Ex);
                            MRequestBase mrequest = new MRequestBase();
                            mrequest.User = "subin";
                            mrequest.Data = ExitStr;
                            mrequest.Method = "exit";
                            mrequest.Version = "1.0";
                            mrequest.RequestToken = Guid.NewGuid().ToString();
                            mrequest.TimeStamp = GetTimeStamp();
                            mrequest = ReturnMRequestBase(mrequest);
                            string RequestJson = JsonConvert.SerializeObject(mrequest);
                            LogWrapper.WriteInfo("Send exit Json:" + RequestJson);
                            string result = MessageUploader.PostJson(RequestJson, configinfo.POSTURL);
                            if (!string.IsNullOrEmpty(result))
                            {
                                try
                                {
                                    result = result.Replace(@"\", "");
                                    int begin = result.IndexOf('{');
                                    int end = result.LastIndexOf('}');
                                    result = result.Substring(begin, end);
                                    MResponseBase Rresult = JsonConvert.DeserializeObject<MResponseBase>(result);
                                    if (Rresult.Success == true)
                                    {
                                        LogWrapper.WriteInfo("Send exit Json Success " );
                                    }
                                    else
                                    {
                                        LogWrapper.WriteInfo("Send exit Json fault " );
                                    }
                                }
                                catch(Exception ex)
                                {
                                    LogWrapper.WriteError(ex.ToString());
                                }
                            }
                            else
                            {
                                LogWrapper.WriteInfo("Send exit Json fault " );
                            }
                        }
                    }
                    catch (Exception em)
                    {
                        LogWrapper.WriteError(em.ToString());
                    }
                }
            }

        }
        private MRequestBase ReturnMRequestBase(MRequestBase mrequest)
        {
            MRequestBase mrequest1 =new MRequestBase();
            mrequest1 = mrequest;
            string StrSign=string.Format("user='{0}'&timestamp='{1}'&version='{2}'&requesttoken='{3}'&method='{4}'&data='{5}'",
                mrequest.User,mrequest.TimeStamp,mrequest.Version,mrequest.RequestToken,mrequest.Method,mrequest.Data);
            string MD5Str = UserMd5(StrSign+DateTime.Now.ToString("yyyy-MM-dd")+configinfo.Serect);
            mrequest1.Sign = MD5Str;
            return mrequest1;
        }
        private string UserMd5(string str)
        {
            string cl = str;
            string pwd = "";
            MD5 md5 = MD5.Create();//实例化一个md5对像
            // 加密后是一个字节类型的数组，这里要注意编码UTF8/Unicode等的选择　
            byte[] s = md5.ComputeHash(Encoding.UTF8.GetBytes(cl));
            // 通过使用循环，将字节类型的数组转换为字符串，此字符串是常规字符格式化所得
            for (int i = 0; i < s.Length; i++)
            {
                // 将得到的字符串使用十六进制类型格式。格式后的字符是小写的字母，如果使用大写（X）则格式后的字符是大写字符 

                pwd = pwd + s[i].ToString("x");

            }
            return pwd;
        }
        private void UpdataParkingInfo(string NodeName, string NewNumber)
        {
            try
            {
                XmlDocument xmlDocument = new XmlDocument();
                xmlDocument.Load(AppDomain.CurrentDomain.BaseDirectory + @"\ParkingInfo.xml");
                XmlNodeList xnl = xmlDocument.SelectSingleNode("NumberInfo").ChildNodes;
                foreach (XmlNode xn in xnl)
                {
                    if (xn.Name == NodeName)
                    {
                        xn.InnerText = NewNumber;
                    }
                }
                xmlDocument.Save(AppDomain.CurrentDomain.BaseDirectory + @"\ParkingInfo.xml");
            }
            catch (Exception ex)
            { LogWrapper.WriteError(ex.ToString()); }
        }
        private MSpaceInfo GetSpaceInfo()
        {
            MSpaceInfo SP = new MSpaceInfo();
            try
            {
                XmlDocument xmlDocument = new XmlDocument();
                xmlDocument.Load(AppDomain.CurrentDomain.BaseDirectory + @"\ParkingInfo.xml");
                XmlNodeList xnl = xmlDocument.SelectSingleNode("NumberInfo").ChildNodes;
                foreach (XmlNode xn in xnl)
                {
                    if (xn.Name == "TSpace")
                    {
                        try
                        {
                           SP.TSpace = Convert.ToInt32(xn.InnerText);
                        }
                        catch
                        {
                            SP.TSpace = 0;
                        }
                    }
                    if (xn.Name == "FTemp")
                    {
                        try
                        {
                            SP.FTemp = Convert.ToInt32(xn.InnerText);
                        }
                        catch
                        {
                            SP.FTemp = 0;
                        }
                    }
                    if (xn.Name == "TMonthly")
                    {
                        try
                        {
                            SP.TMonthly = Convert.ToInt32(xn.InnerText);
                        }
                        catch
                        {
                            SP.TMonthly = 0;
                        }
                    }
                    if (xn.Name == "FMonthly")
                    {
                        try
                        {
                            SP.FMonthly = Convert.ToInt32(xn.InnerText);
                        }
                        catch
                        {
                            SP.FMonthly = 0;
                        }
                    }
                    if (xn.Name == "TTemp")
                    {
                        try
                        {
                            SP.TTemp = Convert.ToInt32(xn.InnerText);
                        }
                        catch
                        {
                            SP.TTemp = 0;
                        }
                    }
                  
                }
                SP.FSpace = SP.FTemp + SP.FMonthly;
            }
            catch (Exception ex)
            { LogWrapper.WriteError(ex.ToString()); }
            return SP;
        }
        public string GetTimeStamp()
        {
            TimeSpan ts = DateTime.UtcNow - new DateTime(1970, 1, 1, 0, 0, 0, 0);
            return Convert.ToInt64(ts.TotalSeconds).ToString();
        }  
        public void Stop()
        {
            throw new NotImplementedException();
        }

        #endregion
    }
}
