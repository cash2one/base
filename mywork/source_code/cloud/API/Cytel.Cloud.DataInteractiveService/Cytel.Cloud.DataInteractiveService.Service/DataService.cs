// ***********************************************************************
// Assembly         : Cytel.Cloud.DataInteractiveService.Service
// Author           : jack
// Created          : 07-14-2016
//
// Last Modified By : jack
// Last Modified On : 07-14-2016
// ***********************************************************************
// <copyright file="DataInteractiveService.cs" company="Cytel">
//     Copyright (c) Cytel. All rights reserved.
// </copyright>
// <summary>DataInteractiveService<summary>
// ***********************************************************************
using System;
using System.Collections.Generic;
using System.Configuration;
using System.Linq;
using System.Text;
using Cytel.Cloud.DataInteractiveService.BizIF;
using Cytel.Cloud.DataInteractiveService.Contract;
using Cytel.Common.Json;
using Microsoft.Practices.Unity;
using Microsoft.Practices.Unity.Configuration;


/// <summary>
/// The Service namespace.
/// </summary>
namespace Cytel.Cloud.DataInteractiveService.Service
{
    /// <summary>
    /// Class DataInteractiveService.
    /// </summary>
    public class DataService : IDataService
    {
        /// <summary>
        /// The mycontainer
        /// </summary>
        private IUnityContainer mycontainer = new UnityContainer();
        /// <summary>
        /// The task
        /// </summary>
        private ITask task;

        #region IDataInteractiveService 成员

        /// <summary>
        /// 上传数据.
        /// </summary>
        /// <param name="req">请求Json字符串.</param>
        /// <returns>响应Json字符串.</returns>
        public string UploadData(MRequestBase req)
        {
            string strResp = string.Empty;
            strResp = ExecuteTask(JsonConvert.SerializeObject(req));
            return strResp;
        }

        /// <summary>
        /// Executes the task.
        /// </summary>
        /// <param name="strReq">The string req.</param>
        /// <returns>System.String.</returns>
        private string ExecuteTask(string strReq)
        {
            //配置文件注册
            UnityConfigurationSection section = (UnityConfigurationSection)ConfigurationManager.GetSection("unity");
            section.Configure(mycontainer);

            //调用依赖
            task = mycontainer.Resolve<ITask>();
            return task.Execute(strReq);
        }

        #endregion
    }
}
