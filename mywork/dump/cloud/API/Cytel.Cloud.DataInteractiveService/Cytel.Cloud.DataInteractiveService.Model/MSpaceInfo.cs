// ***********************************************************************
// Assembly         : Cytel.Cloud.DataInteractiveService.Model
// Author           : jack
// Created          : 07-14-2016
//
// Last Modified By : jack
// Last Modified On : 07-14-2016
// ***********************************************************************
// <copyright file="MSpaceInfo.cs" company="Cytel">
//     Copyright (c) Cytel. All rights reserved.
// </copyright>
// <summary>MSpaceInfo<summary>
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
    /// Class MSpaceInfo.
    /// </summary>
    public class MSpaceInfo
    {
        /// <summary>
        /// 总停车位.
        /// </summary>
        /// <value>The attribute space.</value>
        public int TSpace { get; set; }

        /// <summary>
        /// 月租长包总车位.
        /// </summary>
        /// <value>The attribute monthly.</value>
        public int TMonthly { get; set; }

        /// <summary>
        /// 时租访客总车位.
        /// </summary>
        /// <value>The attribute temporary.</value>
        public int TTemp { get; set; }

        /// <summary>
        /// 总剩余空位.
        /// </summary>
        /// <value>The configuration space.</value>
        public int FSpace { get; set; }

        /// <summary>
        /// 月租长包剩余车位.
        /// </summary>
        /// <value>The configuration monthly.</value>
        public int FMonthly { get; set; }

        /// <summary>
        /// 时租访客剩余车位.
        /// </summary>
        /// <value>The configuration temporary.</value>
        public int FTemp { get; set; }
    }
}
