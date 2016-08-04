<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="15008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="From ByteArray.vi" Type="VI" URL="../../../../superKSDK/05_Labview Driver/Examples/From ByteArray.vi"/>
		<Item Name="getSuperKControls.vi" Type="VI" URL="../getSuperKControls.vi"/>
		<Item Name="getSuperKInfo.vi" Type="VI" URL="../getSuperKInfo.vi"/>
		<Item Name="getSuperKReadings.vi" Type="VI" URL="../getSuperKReadings.vi"/>
		<Item Name="getSuperKStatusBits.vi" Type="VI" URL="../getSuperKStatusBits.vi"/>
		<Item Name="getVariaControls.vi" Type="VI" URL="../getVariaControls.vi"/>
		<Item Name="getVariaInfo.vi" Type="VI" URL="../getVariaInfo.vi"/>
		<Item Name="getVariaReadings.vi" Type="VI" URL="../getVariaReadings.vi"/>
		<Item Name="getVariaStatusBits.vi" Type="VI" URL="../getVariaStatusBits.vi"/>
		<Item Name="portClose.vi" Type="VI" URL="../portClose.vi"/>
		<Item Name="portOpen.vi" Type="VI" URL="../portOpen.vi"/>
		<Item Name="portUtil.vi" Type="VI" URL="../portUtil.vi"/>
		<Item Name="setSuperKControlEmission.vi" Type="VI" URL="../setSuperKControlEmission.vi"/>
		<Item Name="setSuperKControlInterlock.vi" Type="VI" URL="../setSuperKControlInterlock.vi"/>
		<Item Name="setSuperKControls.vi" Type="VI" URL="../setSuperKControls.vi"/>
		<Item Name="setVariaControls.vi" Type="VI" URL="../setVariaControls.vi"/>
		<Item Name="To ByteArray.vi" Type="VI" URL="../../../../superKSDK/05_Labview Driver/Examples/To ByteArray.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="Select Event Type.ctl" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/Select Event Type.ctl"/>
				<Item Name="VISA Configure Serial Port" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port"/>
				<Item Name="VISA Configure Serial Port (Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Instr).vi"/>
				<Item Name="VISA Configure Serial Port (Serial Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Serial Instr).vi"/>
				<Item Name="VISA Flush IO Buffer Mask.ctl" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Flush IO Buffer Mask.ctl"/>
				<Item Name="VISA Set IO Buffer Mask.ctl" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Set IO Buffer Mask.ctl"/>
			</Item>
			<Item Name="From ByteArray ([SGL]).vi" Type="VI" URL="../../../../superKSDK/05_Labview Driver/Examples/From ByteArray ([SGL]).vi"/>
			<Item Name="From ByteArray ([U16]).vi" Type="VI" URL="../../../../superKSDK/05_Labview Driver/Examples/From ByteArray ([U16]).vi"/>
			<Item Name="From ByteArray ([U32]).vi" Type="VI" URL="../../../../superKSDK/05_Labview Driver/Examples/From ByteArray ([U32]).vi"/>
			<Item Name="NGSerialPort.vi" Type="VI" URL="../../../../superKSDK/05_Labview Driver/NGSerialPort.vi"/>
			<Item Name="NGSerialPort_global.vi" Type="VI" URL="../../../../superKSDK/05_Labview Driver/NGSerialPort_global.vi"/>
			<Item Name="To ByteArray ([SGL]).vi" Type="VI" URL="../../../../superKSDK/05_Labview Driver/Examples/To ByteArray ([SGL]).vi"/>
			<Item Name="To ByteArray ([U16]).vi" Type="VI" URL="../../../../superKSDK/05_Labview Driver/Examples/To ByteArray ([U16]).vi"/>
			<Item Name="To ByteArray ([U32]).vi" Type="VI" URL="../../../../superKSDK/05_Labview Driver/Examples/To ByteArray ([U32]).vi"/>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="superKUtil" Type="DLL">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{B947FF37-4FF3-4477-A36A-07AE9660E2A3}</Property>
				<Property Name="App_INI_GUID" Type="Str">{58B5C842-46B5-4CEE-910C-17AD40F93206}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{76B3CBF7-4385-4266-AE93-ACBAD78B3D8A}</Property>
				<Property Name="Bld_buildSpecDescription" Type="Str">Functions to control NKP Supercontrinuum laser (using LV drivers).
Jeff Lidgard, Feb 2016.</Property>
				<Property Name="Bld_buildSpecName" Type="Str">superKUtil</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">..</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{08F63161-54AE-451D-A0B9-D4F9EC5C3A07}</Property>
				<Property Name="Bld_supportedLanguage[0]" Type="Str">English</Property>
				<Property Name="Bld_supportedLanguageCount" Type="Int">1</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">superKUtil.dll</Property>
				<Property Name="Destination[0].path" Type="Path">../superKUtil.dll</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">..</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Dll_compatibilityWith2011" Type="Bool">false</Property>
				<Property Name="Dll_delayOSMsg" Type="Bool">true</Property>
				<Property Name="Dll_headerGUID" Type="Str">{09EDC7AE-E027-45E8-A78B-2B95859527BE}</Property>
				<Property Name="Dll_includeTypeLibrary" Type="Bool">true</Property>
				<Property Name="Dll_libGUID" Type="Str">{29FD5DD7-5962-4C9A-ABE2-4F46B5CE7D4E}</Property>
				<Property Name="Source[0].itemID" Type="Str">{AA77859C-FA5F-4BDF-887D-3E7EEAE118B7}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/From ByteArray.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="Source[10].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[10].itemID" Type="Ref">/My Computer/getVariaReadings.vi</Property>
				<Property Name="Source[10].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[10].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[11].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[11].itemID" Type="Ref">/My Computer/getVariaStatusBits.vi</Property>
				<Property Name="Source[11].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[11].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[12].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[12].itemID" Type="Ref">/My Computer/portOpen.vi</Property>
				<Property Name="Source[12].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[12].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[13].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[13].itemID" Type="Ref">/My Computer/portUtil.vi</Property>
				<Property Name="Source[13].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[13].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[14].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[14].itemID" Type="Ref">/My Computer/setSuperKControls.vi</Property>
				<Property Name="Source[14].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[14].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[15].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[15].itemID" Type="Ref">/My Computer/setVariaControls.vi</Property>
				<Property Name="Source[15].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[15].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[16].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[16].itemID" Type="Ref">/My Computer/setSuperKControlEmission.vi</Property>
				<Property Name="Source[16].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[16].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[17].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[17].itemID" Type="Ref">/My Computer/setSuperKControlInterlock.vi</Property>
				<Property Name="Source[17].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[17].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[2].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[2].itemID" Type="Ref">/My Computer/portClose.vi</Property>
				<Property Name="Source[2].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[2].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[3].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[3].itemID" Type="Ref">/My Computer/To ByteArray.vi</Property>
				<Property Name="Source[3].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[3].type" Type="Str">VI</Property>
				<Property Name="Source[4].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[4].itemID" Type="Ref">/My Computer/getSuperKControls.vi</Property>
				<Property Name="Source[4].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[4].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[5].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[0]VIProtoDir" Type="Int">4</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[0]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[0]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[0]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[0]VIProtoName" Type="Str">return value</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[0]VIProtoOutputIdx" Type="Int">0</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[0]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[1]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[1]VIProtoInputIdx" Type="Int">11</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[1]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[1]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[1]VIProtoName" Type="Str">COMport</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[1]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[1]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[2]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[2]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[2]VIProtoLenInput" Type="Int">3</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[2]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[2]VIProtoName" Type="Str">moduleSerialNumber</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[2]VIProtoOutputIdx" Type="Int">5</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[2]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[3]VIProtoDir" Type="Int">3</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[3]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[3]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[3]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[3]VIProtoName" Type="Str">len</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[3]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[3]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[4]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[4]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[4]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[4]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[4]VIProtoName" Type="Str">moduleType</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[4]VIProtoOutputIdx" Type="Int">4</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[4]VIProtoPassBy" Type="Int">0</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[5]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[5]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[5]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[5]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[5]VIProtoName" Type="Str">firmwareVersion</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[5]VIProtoOutputIdx" Type="Int">2</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[5]VIProtoPassBy" Type="Int">0</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[6]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[6]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[6]VIProtoLenInput" Type="Int">7</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[6]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[6]VIProtoName" Type="Str">extendedVersionInfo</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[6]VIProtoOutputIdx" Type="Int">1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[6]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[7]CallingConv" Type="Int">1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[7]Name" Type="Str">GetSuperKInfo</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[7]VIProtoDir" Type="Int">3</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[7]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[7]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[7]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[7]VIProtoName" Type="Str">len2</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[7]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfo[7]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfoCPTM" Type="Bin">&amp;!#!!!!!!!Q!$%!B"H.U982V=Q!!#U!$!!2D&lt;W2F!!!11$$`````"H.P&gt;8*D:1!!&amp;E"1!!-!!!!"!!)*:8*S&lt;X)A&lt;X6U!"R!-0````]4:8BU:7ZE:727:8*T;7^O37ZG&lt;Q!61!9!$W:J=GVX98*F6G6S=WFP&lt;A!%!!!!%5!$!!JN&lt;W2V&lt;'65?8"F!!!=1$$`````%GVP:(6M:6.F=GFB&lt;%ZV&lt;7*F=A!!)%"1!!-!!!!"!!)4:8*S&lt;X)A;7YA+'ZP)'6S=G^S+1!11$$`````"U.048"P=H1!6!$Q!!Q!!Q!%!!5!"A!(!!A!"A!'!!E!"A!'!!I$!!"Y!!!*!!!!#1!!!!E!!!!!!!!!#1!!!!E!!!!!!!!!!!!!!!I!!!!!!!!!!!!!!AA!!!!!!1!,</Property>
				<Property Name="Source[5].ExportedVI.VIProtoInfoVIProtoItemCount" Type="Int">8</Property>
				<Property Name="Source[5].itemID" Type="Ref">/My Computer/getSuperKInfo.vi</Property>
				<Property Name="Source[5].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[5].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[6].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[6].itemID" Type="Ref">/My Computer/getSuperKReadings.vi</Property>
				<Property Name="Source[6].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[6].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[7].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[7].itemID" Type="Ref">/My Computer/getSuperKStatusBits.vi</Property>
				<Property Name="Source[7].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[7].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[8].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[8].itemID" Type="Ref">/My Computer/getVariaControls.vi</Property>
				<Property Name="Source[8].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[8].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[9].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[0]VIProtoDir" Type="Int">4</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[0]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[0]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[0]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[0]VIProtoName" Type="Str">return value</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[0]VIProtoOutputIdx" Type="Int">0</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[0]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[1]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[1]VIProtoInputIdx" Type="Int">11</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[1]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[1]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[1]VIProtoName" Type="Str">COMport</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[1]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[1]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[2]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[2]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[2]VIProtoLenInput" Type="Int">3</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[2]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[2]VIProtoName" Type="Str">moduleSerialNumber</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[2]VIProtoOutputIdx" Type="Int">5</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[2]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[3]VIProtoDir" Type="Int">3</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[3]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[3]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[3]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[3]VIProtoName" Type="Str">len</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[3]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[3]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[4]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[4]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[4]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[4]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[4]VIProtoName" Type="Str">moduleType</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[4]VIProtoOutputIdx" Type="Int">4</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[4]VIProtoPassBy" Type="Int">0</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[5]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[5]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[5]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[5]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[5]VIProtoName" Type="Str">firmwareVersion</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[5]VIProtoOutputIdx" Type="Int">2</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[5]VIProtoPassBy" Type="Int">0</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[6]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[6]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[6]VIProtoLenInput" Type="Int">7</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[6]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[6]VIProtoName" Type="Str">extendedVersionInfo</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[6]VIProtoOutputIdx" Type="Int">1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[6]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[7]CallingConv" Type="Int">1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[7]Name" Type="Str">GetVariaInfo</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[7]VIProtoDir" Type="Int">3</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[7]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[7]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[7]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[7]VIProtoName" Type="Str">len2</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[7]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfo[7]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfoCPTM" Type="Bin">&amp;!#!!!!!!!Q!$%!B"H.U982V=Q!!#U!$!!2D&lt;W2F!!!11$$`````"H.P&gt;8*D:1!!&amp;E"1!!-!!!!"!!)*:8*S&lt;X)A&lt;X6U!"R!-0````]4:8BU:7ZE:727:8*T;7^O37ZG&lt;Q!61!9!$W:J=GVX98*F6G6S=WFP&lt;A!%!!!!%5!$!!JN&lt;W2V&lt;'65?8"F!!!=1$$`````%GVP:(6M:6.F=GFB&lt;%ZV&lt;7*F=A!!)%"1!!-!!!!"!!)4:8*S&lt;X)A;7YA+'ZP)'6S=G^S+1!11$$`````"U.048"P=H1!6!$Q!!Q!!Q!%!!5!"A!(!!A!"A!'!!E!"A!'!!I$!!"Y!!!*!!!!#1!!!!E!!!!!!!!!#1!!!!E!!!!!!!!!!!!!!!I!!!!!!!!!!!!!!AA!!!!!!1!,</Property>
				<Property Name="Source[9].ExportedVI.VIProtoInfoVIProtoItemCount" Type="Int">8</Property>
				<Property Name="Source[9].itemID" Type="Ref">/My Computer/getVariaInfo.vi</Property>
				<Property Name="Source[9].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[9].type" Type="Str">ExportedVI</Property>
				<Property Name="SourceCount" Type="Int">18</Property>
				<Property Name="TgtF_companyName" Type="Str">Oxford University Department Of Physics</Property>
				<Property Name="TgtF_fileDescription" Type="Str">Functions to control NKP Supercontrinuum laser (using LV drivers).
Jeff Lidgard, Feb 2016.</Property>
				<Property Name="TgtF_internalName" Type="Str">superKUtil</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2016 Oxford University Department Of Physics</Property>
				<Property Name="TgtF_productName" Type="Str">superKUtil</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{BD059A66-0C30-4E7B-8207-ABBE7C2B10A0}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">superKUtil.dll</Property>
			</Item>
		</Item>
	</Item>
</Project>
