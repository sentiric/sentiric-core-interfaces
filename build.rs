fn main() -> Result<(), Box<dyn std::error::Error>> {
    tonic_build::compile_protos("proto/sentiric/dialplan/v1/dialplan.proto")?;
    tonic_build::compile_protos("proto/sentiric/media/v1/media.proto")?;
    tonic_build::compile_protos("proto/sentiric/user/v1/user.proto")?;
    Ok(())
}