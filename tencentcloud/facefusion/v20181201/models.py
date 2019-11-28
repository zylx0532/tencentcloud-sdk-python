# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tencentcloud.common.abstract_model import AbstractModel


class FaceFusionRequest(AbstractModel):
    """FaceFusion请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 活动 ID，请在人脸融合控制台查看。
        :type ProjectId: str
        :param ModelId: 素材 ID，请在人脸融合控制台查看。
        :type ModelId: str
        :param Image: 图片 base64 数据。请确保人脸为正脸，无旋转。若某些手机拍摄后人脸被旋转，请使用图片的 EXIF 信息对图片进行旋转处理；请勿在 base64 数据中包含头部，如“data:image/jpeg;base64,”。
        :type Image: str
        :param RspImgType: 返回图像方式（url 或 base64) ，二选一。当前仅支持 url 方式，base64 方式后期开放。
        :type RspImgType: str
        :param PornDetect: 历史遗留字段，无需填写。因为融合只需提取人脸特征，不需要鉴黄。
        :type PornDetect: int
        :param CelebrityIdentify: 0表示不需要鉴政，1表示需要鉴政。默认值为0。
        :type CelebrityIdentify: int
        """
        self.ProjectId = None
        self.ModelId = None
        self.Image = None
        self.RspImgType = None
        self.PornDetect = None
        self.CelebrityIdentify = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ModelId = params.get("ModelId")
        self.Image = params.get("Image")
        self.RspImgType = params.get("RspImgType")
        self.PornDetect = params.get("PornDetect")
        self.CelebrityIdentify = params.get("CelebrityIdentify")


class FaceFusionResponse(AbstractModel):
    """FaceFusion返回参数结构体

    """

    def __init__(self):
        """
        :param Image: RspImgType 为 url 时，返回结果的 url， RspImgType 为 base64 时返回 base64 数据。当前仅支持 url 方式，base64 方式后期开放。
        :type Image: str
        :param ReviewResultSet: 鉴政结果
        :type ReviewResultSet: list of FuseFaceReviewResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Image = None
        self.ReviewResultSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        if params.get("ReviewResultSet") is not None:
            self.ReviewResultSet = []
            for item in params.get("ReviewResultSet"):
                obj = FuseFaceReviewResult()
                obj._deserialize(item)
                self.ReviewResultSet.append(obj)
        self.RequestId = params.get("RequestId")


class FaceRect(AbstractModel):
    """人脸框信息

    """

    def __init__(self):
        """
        :param X: 人脸框左上角横坐标。
        :type X: int
        :param Y: 人脸框左上角纵坐标。
        :type Y: int
        :param Width: 人脸框宽度。
        :type Width: int
        :param Height: 人脸框高度。
        :type Height: int
        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class FuseFaceRequest(AbstractModel):
    """FuseFace请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 活动 ID，请在人脸融合控制台查看。
        :type ProjectId: str
        :param ModelId: 素材 ID，请在人脸融合控制台查看。
        :type ModelId: str
        :param RspImgType: 返回图像方式（url 或 base64) ，二选一。url有效期为30天。
        :type RspImgType: str
        :param MergeInfos: 用户人脸图片、素材模板图的人脸位置信息。
        :type MergeInfos: list of MergeInfo
        :param FuseProfileDegree: 脸型融合比例，数值越高，融合后的脸型越像素材人物。取值范围[0,100] 
若此参数不填写，则使用人脸融合控制台中脸型参数数值。
        :type FuseProfileDegree: int
        :param FuseFaceDegree: 五官融合比例，数值越高，融合后的五官越像素材人物。取值范围[0,100] 
若此参数不填写，则使用人脸融合控制台中五官参数数值。
        :type FuseFaceDegree: int
        :param CelebrityIdentify: 0表示不需要鉴政，1表示需要鉴政。默认值为0。
        :type CelebrityIdentify: int
        """
        self.ProjectId = None
        self.ModelId = None
        self.RspImgType = None
        self.MergeInfos = None
        self.FuseProfileDegree = None
        self.FuseFaceDegree = None
        self.CelebrityIdentify = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ModelId = params.get("ModelId")
        self.RspImgType = params.get("RspImgType")
        if params.get("MergeInfos") is not None:
            self.MergeInfos = []
            for item in params.get("MergeInfos"):
                obj = MergeInfo()
                obj._deserialize(item)
                self.MergeInfos.append(obj)
        self.FuseProfileDegree = params.get("FuseProfileDegree")
        self.FuseFaceDegree = params.get("FuseFaceDegree")
        self.CelebrityIdentify = params.get("CelebrityIdentify")


class FuseFaceResponse(AbstractModel):
    """FuseFace返回参数结构体

    """

    def __init__(self):
        """
        :param FusedImage: RspImgType 为 url 时，返回结果的 url， RspImgType 为 base64 时返回 base64 数据。
        :type FusedImage: str
        :param ReviewResultSet: 鉴政结果。该数组的顺序和请求中mergeinfo的顺序一致，一一对应
注意：此字段可能返回 null，表示取不到有效值。
        :type ReviewResultSet: list of FuseFaceReviewResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FusedImage = None
        self.ReviewResultSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FusedImage = params.get("FusedImage")
        if params.get("ReviewResultSet") is not None:
            self.ReviewResultSet = []
            for item in params.get("ReviewResultSet"):
                obj = FuseFaceReviewResult()
                obj._deserialize(item)
                self.ReviewResultSet.append(obj)
        self.RequestId = params.get("RequestId")


class FuseFaceReviewDetail(AbstractModel):
    """人脸融合鉴黄鉴政人脸信息

    """

    def __init__(self):
        """
        :param Field: 保留字段
        :type Field: str
        :param Label: 人员名称
        :type Label: str
        :param Confidence: 对应识别label的置信度，分数越高意味涉政可能性越大。 
0到70，Suggestion建议为PASS； 
70到80，Suggestion建议为REVIEW； 
80到100，Suggestion建议为BLOCK。
        :type Confidence: float
        :param Suggestion: 识别场景的审核结论：  
PASS：正常 
REVIEW：疑似  
BLOCK：违规
        :type Suggestion: str
        """
        self.Field = None
        self.Label = None
        self.Confidence = None
        self.Suggestion = None


    def _deserialize(self, params):
        self.Field = params.get("Field")
        self.Label = params.get("Label")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")


class FuseFaceReviewResult(AbstractModel):
    """人脸融合鉴黄鉴政返回参数item

    """

    def __init__(self):
        """
        :param Category: 保留字段
        :type Category: str
        :param Code: 状态码， 0为处理成功，其他值为处理失败
        :type Code: str
        :param CodeDescription: 对应状态码信息描述
        :type CodeDescription: str
        :param Confidence: 保留字段
        :type Confidence: float
        :param Suggestion: 保留字段
        :type Suggestion: str
        :param DetailSet: 审核详细内容
        :type DetailSet: list of FuseFaceReviewDetail
        """
        self.Category = None
        self.Code = None
        self.CodeDescription = None
        self.Confidence = None
        self.Suggestion = None
        self.DetailSet = None


    def _deserialize(self, params):
        self.Category = params.get("Category")
        self.Code = params.get("Code")
        self.CodeDescription = params.get("CodeDescription")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("DetailSet") is not None:
            self.DetailSet = []
            for item in params.get("DetailSet"):
                obj = FuseFaceReviewDetail()
                obj._deserialize(item)
                self.DetailSet.append(obj)


class MergeInfo(AbstractModel):
    """人脸图片和待被融合的素材模板图的人脸位置信息。

    """

    def __init__(self):
        """
        :param Image: 输入图片base64
        :type Image: str
        :param Url: 输入图片url
        :type Url: str
        :param InputImageFaceRect: 上传的图片人脸位置信息（人脸框）
        :type InputImageFaceRect: :class:`tencentcloud.facefusion.v20181201.models.FaceRect`
        :param TemplateFaceID: 控制台上传的素材人脸ID
        :type TemplateFaceID: str
        """
        self.Image = None
        self.Url = None
        self.InputImageFaceRect = None
        self.TemplateFaceID = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        if params.get("InputImageFaceRect") is not None:
            self.InputImageFaceRect = FaceRect()
            self.InputImageFaceRect._deserialize(params.get("InputImageFaceRect"))
        self.TemplateFaceID = params.get("TemplateFaceID")