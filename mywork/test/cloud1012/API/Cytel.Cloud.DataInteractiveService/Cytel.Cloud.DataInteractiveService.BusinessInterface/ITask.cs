// ***********************************************************************
// Assembly         : Cytel.Cloud.DataInteractiveService.BizIF
// Author           : jack
// Created          : 07-14-2016
//
// Last Modified By : jack
// Last Modified On : 07-14-2016
// ***********************************************************************
// <copyright file="ITask.cs" company="Cytel">
//     Copyright (c) Cytel. All rights reserved.
// </copyright>
// <summary>ITask<summary>
// ***********************************************************************
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Cytel.Cloud.DataInteractiveService.Model;

/// <summary>
/// The BusinessInterface namespace.
/// </summary>
namespace Cytel.Cloud.DataInteractiveService.BizIF
{
    /// <summary>
    /// Interface ITask
    /// </summary>
    public interface ITask
    {
        /// <summary>
        /// Executes the specified string req.
        /// </summary>
        /// <param name="strReq">The string req.</param>
        /// <returns>System.String.</returns>
        string Execute(string strReq);
    }
}
