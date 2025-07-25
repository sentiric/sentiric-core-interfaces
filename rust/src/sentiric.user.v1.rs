// @generated
// This file is @generated by prost-build.
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct AuthenticateUserRequest {
    /// Arayanın SIP URI'si, örn: "sip:1001@domain.com"
    #[prost(string, tag="1")]
    pub from_uri: ::prost::alloc::string::String,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct AuthenticateUserResponse {
    #[prost(enumeration="authenticate_user_response::Status", tag="1")]
    pub status: i32,
    /// Doğrulama başarılıysa, sistemdeki kullanıcı ID'si
    #[prost(string, tag="2")]
    pub user_id: ::prost::alloc::string::String,
    /// Kullanıcının ait olduğu müşteri ID'si
    #[prost(string, tag="3")]
    pub tenant_id: ::prost::alloc::string::String,
}
/// Nested message and enum types in `AuthenticateUserResponse`.
pub mod authenticate_user_response {
    #[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, PartialOrd, Ord, ::prost::Enumeration)]
    #[repr(i32)]
    pub enum Status {
        Unspecified = 0,
        Ok = 1,
        NotFound = 2,
        Failed = 3,
    }
    impl Status {
        /// String value of the enum field names used in the ProtoBuf definition.
        ///
        /// The values are not transformed in any way and thus are considered stable
        /// (if the ProtoBuf definition does not change) and safe for programmatic use.
        pub fn as_str_name(&self) -> &'static str {
            match self {
                Self::Unspecified => "STATUS_UNSPECIFIED",
                Self::Ok => "STATUS_OK",
                Self::NotFound => "STATUS_NOT_FOUND",
                Self::Failed => "STATUS_FAILED",
            }
        }
        /// Creates an enum from field names used in the ProtoBuf definition.
        pub fn from_str_name(value: &str) -> ::core::option::Option<Self> {
            match value {
                "STATUS_UNSPECIFIED" => Some(Self::Unspecified),
                "STATUS_OK" => Some(Self::Ok),
                "STATUS_NOT_FOUND" => Some(Self::NotFound),
                "STATUS_FAILED" => Some(Self::Failed),
                _ => None,
            }
        }
    }
}
// @@protoc_insertion_point(module)
