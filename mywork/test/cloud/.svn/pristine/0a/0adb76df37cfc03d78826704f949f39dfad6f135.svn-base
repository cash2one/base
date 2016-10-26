// ***********************************************************************
// Assembly         : Cytel.Cloud.DataInteractiveService.Contract
// Author           : jack
// Created          : 07-14-2016
//
// Last Modified By : jack
// Last Modified On : 07-14-2016
// ***********************************************************************
// <copyright file="IDataInteractiveService.cs" company="Cytel">
//     Copyright (c) Cytel. All rights reserved.
// </copyright>
// <summary>IDataInteractiveService<summary>
// ***********************************************************************
using System;
using System.Collections.Generic;
using System.Linq;
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Text;

/// <summary>
/// The Contract namespace.
/// </summary>
namespace Cytel.Cloud.DataInteractiveService.Contract
{
    /// <summary>
    /// Interface IDataInteractiveService
    /// </summary>
    [ServiceContract]
    public interface IDataService
    {
        /// <summary>
        /// 上传数据.
        /// </summary>
        /// <param name="strReq">请求Json字符串.</param>
        /// <returns>响应Json字符串.</returns>
        [OperationContract]
        [WebInvoke(UriTemplate = "service/api/v1/uploaddata", Method = "POST",
            RequestFormat = WebMessageFormat.Json, ResponseFormat = WebMessageFormat.Json, BodyStyle = WebMessageBodyStyle.Bare)]
        string UploadData(MRequestBase req);
    }
}
