// ***********************************************************************
// Assembly         : Cytel.Cloud.DataInteractiveService.Model
// Author           : jack
// Created          : 07-14-2016
//
// Last Modified By : jack
// Last Modified On : 07-14-2016
// ***********************************************************************
// <copyright file="MResponseCode.cs" company="Cytel">
//     Copyright (c) Cytel. All rights reserved.
// </copyright>
// <summary>MResponseCode<summary>
// ***********************************************************************
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

/// <summary>
/// The Model namespace.
/// </summary>
namespace Cytel.Cloud.DataInteractiveService.Model
{
    /// <summary>
    /// Enum MResponseCode
    /// </summary>
    public enum MResponseCode
    {
        /// <summary>
        /// The success
        /// </summary>
        Success = 0,

        /// <summary>
        /// The system error
        /// </summary>
        SysError = 9999,

        /// <summary>
        /// The method not found
        /// </summary>
        MethodNotFound = 10009,

        /// <summary>
        /// The parameter error
        /// </summary>
        ParamError = 20001
    }
}
