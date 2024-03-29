// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: CommandService.proto
// </auto-generated>
#pragma warning disable 0414, 1591
#region Designer generated code

using grpc = global::Grpc.Core;

namespace QuoteResearch.Service.CommandService {
  public static partial class CommandService
  {
    static readonly string __ServiceName = "QuoteResearch.Service.CommandService.CommandService";

    static readonly grpc::Marshaller<global::QuoteResearch.Service.Share.Type.EmptyRequest> __Marshaller_QuoteResearch_Service_Share_Type_EmptyRequest = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::QuoteResearch.Service.Share.Type.EmptyRequest.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::QuoteResearch.Service.CommandService.CommandServiceResponse> __Marshaller_QuoteResearch_Service_CommandService_CommandServiceResponse = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::QuoteResearch.Service.CommandService.CommandServiceResponse.Parser.ParseFrom);

    static readonly grpc::Method<global::QuoteResearch.Service.Share.Type.EmptyRequest, global::QuoteResearch.Service.CommandService.CommandServiceResponse> __Method_Start = new grpc::Method<global::QuoteResearch.Service.Share.Type.EmptyRequest, global::QuoteResearch.Service.CommandService.CommandServiceResponse>(
        grpc::MethodType.Unary,
        __ServiceName,
        "Start",
        __Marshaller_QuoteResearch_Service_Share_Type_EmptyRequest,
        __Marshaller_QuoteResearch_Service_CommandService_CommandServiceResponse);

    static readonly grpc::Method<global::QuoteResearch.Service.Share.Type.EmptyRequest, global::QuoteResearch.Service.CommandService.CommandServiceResponse> __Method_Stop = new grpc::Method<global::QuoteResearch.Service.Share.Type.EmptyRequest, global::QuoteResearch.Service.CommandService.CommandServiceResponse>(
        grpc::MethodType.Unary,
        __ServiceName,
        "Stop",
        __Marshaller_QuoteResearch_Service_Share_Type_EmptyRequest,
        __Marshaller_QuoteResearch_Service_CommandService_CommandServiceResponse);

    static readonly grpc::Method<global::QuoteResearch.Service.Share.Type.EmptyRequest, global::QuoteResearch.Service.CommandService.CommandServiceResponse> __Method_Restart = new grpc::Method<global::QuoteResearch.Service.Share.Type.EmptyRequest, global::QuoteResearch.Service.CommandService.CommandServiceResponse>(
        grpc::MethodType.Unary,
        __ServiceName,
        "Restart",
        __Marshaller_QuoteResearch_Service_Share_Type_EmptyRequest,
        __Marshaller_QuoteResearch_Service_CommandService_CommandServiceResponse);

    /// <summary>Service descriptor</summary>
    public static global::Google.Protobuf.Reflection.ServiceDescriptor Descriptor
    {
      get { return global::QuoteResearch.Service.CommandService.CommandServiceReflection.Descriptor.Services[0]; }
    }

    /// <summary>Base class for server-side implementations of CommandService</summary>
    [grpc::BindServiceMethod(typeof(CommandService), "BindService")]
    public abstract partial class CommandServiceBase
    {
      /// <summary>
      /// Quote service connection action. 
      /// </summary>
      /// <param name="request">The request received from the client.</param>
      /// <param name="context">The context of the server-side call handler being invoked.</param>
      /// <returns>The response to send back to the client (wrapped by a task).</returns>
      public virtual global::System.Threading.Tasks.Task<global::QuoteResearch.Service.CommandService.CommandServiceResponse> Start(global::QuoteResearch.Service.Share.Type.EmptyRequest request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      public virtual global::System.Threading.Tasks.Task<global::QuoteResearch.Service.CommandService.CommandServiceResponse> Stop(global::QuoteResearch.Service.Share.Type.EmptyRequest request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      public virtual global::System.Threading.Tasks.Task<global::QuoteResearch.Service.CommandService.CommandServiceResponse> Restart(global::QuoteResearch.Service.Share.Type.EmptyRequest request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

    }

    /// <summary>Client for CommandService</summary>
    public partial class CommandServiceClient : grpc::ClientBase<CommandServiceClient>
    {
      /// <summary>Creates a new client for CommandService</summary>
      /// <param name="channel">The channel to use to make remote calls.</param>
      public CommandServiceClient(grpc::ChannelBase channel) : base(channel)
      {
      }
      /// <summary>Creates a new client for CommandService that uses a custom <c>CallInvoker</c>.</summary>
      /// <param name="callInvoker">The callInvoker to use to make remote calls.</param>
      public CommandServiceClient(grpc::CallInvoker callInvoker) : base(callInvoker)
      {
      }
      /// <summary>Protected parameterless constructor to allow creation of test doubles.</summary>
      protected CommandServiceClient() : base()
      {
      }
      /// <summary>Protected constructor to allow creation of configured clients.</summary>
      /// <param name="configuration">The client configuration.</param>
      protected CommandServiceClient(ClientBaseConfiguration configuration) : base(configuration)
      {
      }

      /// <summary>
      /// Quote service connection action. 
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="headers">The initial metadata to send with the call. This parameter is optional.</param>
      /// <param name="deadline">An optional deadline for the call. The call will be cancelled if deadline is hit.</param>
      /// <param name="cancellationToken">An optional token for canceling the call.</param>
      /// <returns>The response received from the server.</returns>
      public virtual global::QuoteResearch.Service.CommandService.CommandServiceResponse Start(global::QuoteResearch.Service.Share.Type.EmptyRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return Start(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      /// <summary>
      /// Quote service connection action. 
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="options">The options for the call.</param>
      /// <returns>The response received from the server.</returns>
      public virtual global::QuoteResearch.Service.CommandService.CommandServiceResponse Start(global::QuoteResearch.Service.Share.Type.EmptyRequest request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_Start, null, options, request);
      }
      /// <summary>
      /// Quote service connection action. 
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="headers">The initial metadata to send with the call. This parameter is optional.</param>
      /// <param name="deadline">An optional deadline for the call. The call will be cancelled if deadline is hit.</param>
      /// <param name="cancellationToken">An optional token for canceling the call.</param>
      /// <returns>The call object.</returns>
      public virtual grpc::AsyncUnaryCall<global::QuoteResearch.Service.CommandService.CommandServiceResponse> StartAsync(global::QuoteResearch.Service.Share.Type.EmptyRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return StartAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      /// <summary>
      /// Quote service connection action. 
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="options">The options for the call.</param>
      /// <returns>The call object.</returns>
      public virtual grpc::AsyncUnaryCall<global::QuoteResearch.Service.CommandService.CommandServiceResponse> StartAsync(global::QuoteResearch.Service.Share.Type.EmptyRequest request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_Start, null, options, request);
      }
      public virtual global::QuoteResearch.Service.CommandService.CommandServiceResponse Stop(global::QuoteResearch.Service.Share.Type.EmptyRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return Stop(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::QuoteResearch.Service.CommandService.CommandServiceResponse Stop(global::QuoteResearch.Service.Share.Type.EmptyRequest request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_Stop, null, options, request);
      }
      public virtual grpc::AsyncUnaryCall<global::QuoteResearch.Service.CommandService.CommandServiceResponse> StopAsync(global::QuoteResearch.Service.Share.Type.EmptyRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return StopAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncUnaryCall<global::QuoteResearch.Service.CommandService.CommandServiceResponse> StopAsync(global::QuoteResearch.Service.Share.Type.EmptyRequest request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_Stop, null, options, request);
      }
      public virtual global::QuoteResearch.Service.CommandService.CommandServiceResponse Restart(global::QuoteResearch.Service.Share.Type.EmptyRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return Restart(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::QuoteResearch.Service.CommandService.CommandServiceResponse Restart(global::QuoteResearch.Service.Share.Type.EmptyRequest request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_Restart, null, options, request);
      }
      public virtual grpc::AsyncUnaryCall<global::QuoteResearch.Service.CommandService.CommandServiceResponse> RestartAsync(global::QuoteResearch.Service.Share.Type.EmptyRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return RestartAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncUnaryCall<global::QuoteResearch.Service.CommandService.CommandServiceResponse> RestartAsync(global::QuoteResearch.Service.Share.Type.EmptyRequest request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_Restart, null, options, request);
      }
      /// <summary>Creates a new instance of client from given <c>ClientBaseConfiguration</c>.</summary>
      protected override CommandServiceClient NewInstance(ClientBaseConfiguration configuration)
      {
        return new CommandServiceClient(configuration);
      }
    }

    /// <summary>Creates service definition that can be registered with a server</summary>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    public static grpc::ServerServiceDefinition BindService(CommandServiceBase serviceImpl)
    {
      return grpc::ServerServiceDefinition.CreateBuilder()
          .AddMethod(__Method_Start, serviceImpl.Start)
          .AddMethod(__Method_Stop, serviceImpl.Stop)
          .AddMethod(__Method_Restart, serviceImpl.Restart).Build();
    }

    /// <summary>Register service method with a service binder with or without implementation. Useful when customizing the  service binding logic.
    /// Note: this method is part of an experimental API that can change or be removed without any prior notice.</summary>
    /// <param name="serviceBinder">Service methods will be bound by calling <c>AddMethod</c> on this object.</param>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    public static void BindService(grpc::ServiceBinderBase serviceBinder, CommandServiceBase serviceImpl)
    {
      serviceBinder.AddMethod(__Method_Start, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::QuoteResearch.Service.Share.Type.EmptyRequest, global::QuoteResearch.Service.CommandService.CommandServiceResponse>(serviceImpl.Start));
      serviceBinder.AddMethod(__Method_Stop, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::QuoteResearch.Service.Share.Type.EmptyRequest, global::QuoteResearch.Service.CommandService.CommandServiceResponse>(serviceImpl.Stop));
      serviceBinder.AddMethod(__Method_Restart, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::QuoteResearch.Service.Share.Type.EmptyRequest, global::QuoteResearch.Service.CommandService.CommandServiceResponse>(serviceImpl.Restart));
    }

  }
}
#endregion
