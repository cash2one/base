using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Configuration;
using System.Data;
using System.Diagnostics;
using System.Linq;
using System.ServiceProcess;
using System.Text;
using Cytel.Cloud.DataUPloadService.ListenerIF;
using Cytel.Common.Log;
using Microsoft.Practices.Unity;
using Microsoft.Practices.Unity.Configuration;

namespace Cytel.Cloud.DataUPloadService.Service
{
    public partial class VBMUploadService : ServiceBase
    {
        private IUnityContainer mycontainer = new UnityContainer();
        private IListener listener;

        public VBMUploadService()
        {
            InitializeComponent();
            InitIOC();
        }

        private void InitIOC()
        {
            //配置文件注册
            UnityConfigurationSection section = (UnityConfigurationSection)ConfigurationManager.GetSection("unity");
            section.Configure(mycontainer);
            //调用依赖
            listener = mycontainer.Resolve<IListener>();
        }

        protected override void OnStart(string[] args)
        {
            LogWrapper.WriteInfo("启动速宾云数据上传服务...");
            AppDomain.CurrentDomain.UnhandledException += new UnhandledExceptionEventHandler(this.CurrentDomain_UnhandledException);
            new Action(listener.Start).BeginInvoke(null, null);
        }

        private void CurrentDomain_UnhandledException(object sender, UnhandledExceptionEventArgs e)
        {
            LogWrapper.WriteFetal(e.ToString());
        }

        protected override void OnStop()
        {
            LogWrapper.WriteInfo("停止速宾云数据上传服务...");
            listener.Stop();
        }
    }
}
