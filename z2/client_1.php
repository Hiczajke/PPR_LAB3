#!/usr/bin/php

<?php
	#===================================================================
	$port 	= 1234;
	$host 	= '127.0.0.1';
	#-------------------------------------------------------------------
	$req = xmlrpc_encode_request(
		"conv", 
		array( array("abc") )
	);
	#-------------------------------------------------------------------
	$ctx = stream_context_create(
		array(
			'http' => array(
				'method' 	=> "POST",
				'header' 	=> array( "Content-Type: text/xml" ),
				'content' 	=> $req
			)
		)
	);
	#-------------------------------------------------------------------
	$xml = file_get_contents( "http://$host:$port/RPC2", false, $ctx );
	#-------------------------------------------------------------------
	$res = xmlrpc_decode( $xml );
	#-------------------------------------------------------------------
	if( $res && xmlrpc_is_fault( $res ) ){
		print "xmlrpc: $res[faultString] ($res[faultCode])";
		exit( 1 );
	} else {
		print_r( $res );
	}
	#===================================================================
?>
