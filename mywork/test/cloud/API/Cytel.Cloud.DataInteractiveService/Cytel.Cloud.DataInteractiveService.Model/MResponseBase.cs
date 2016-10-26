// ***********************************************************************
// Assembly         : Cytel.Cloud.DataInteractiveService.Model
// Author           : jack
// Created          : 07-14-2016
//
// Last Modified By : jack
// Last Modified On : 07-14-2016
// ***********************************************************************
// <copyright file="MResponseBase.cs" company="Cytel">
//     Copyright (c) Cytel. All rights reserved.
// </copyright>
// <summary>MResponseBase<summary>
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
    /// Class MResponseBase.
    /// </summary>
    public class MResponseBase
    {
        /// <summary>
        /// Gets or sets a value indicating whether this <see cref="MResponseBase"/> is success.
        /// </summary>
        /// <value><c>true</c> if success; otherwise, <c>false</c>.</value>
        public bool Success { get; set; }

        /// <summary>
        /// Gets or sets the code.
        /// </summary>
        /// <value>The code.</value>
        public MResponseCode Code { get; set; }

        /// <summary>
        /// Gets or sets the message.
        /// </summary>
        /// <value>The message.</value>
        public string Message { get; set; }

        /// <summary>
        /// Gets or sets the data.
        /// </summary>
        /// <value>The data.</value>
        public string Data { get; set; }

        /// <summary>
        /// Gets or sets the request token.
        /// </summary>
        /// <value>The request token.</value>
        public string RequestToken { get; set; }

        /// <summary>
        /// Gets or sets the sign.
        /// </summary>
        /// <value>The sign.</value>
        public string Sign { get; set; }
    }
}
