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
		<Item Name="OOUtil.lvlib" Type="Library" URL="../OOUtil.lvlib"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="common64.dll" Type="Document" URL="common64.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="OmniDriver64.dll" Type="Document" URL="OmniDriver64.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="OOUtil" Type="DLL">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{0673DCDE-4DD1-4D6F-BD5B-5C45362EA250}</Property>
				<Property Name="App_INI_GUID" Type="Str">{12441A9B-A9E1-4FD5-A6EF-344D8734966B}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{D52644BC-48C8-433A-B877-19DA729E706B}</Property>
				<Property Name="Bld_buildSpecDescription" Type="Str">DLL of spectrometer functions from Ocean Optics</Property>
				<Property Name="Bld_buildSpecName" Type="Str">OOUtil</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">..</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{5BF5855F-537A-46E2-855D-CE1121E9F037}</Property>
				<Property Name="Bld_version.build" Type="Int">21</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">OOUtil.dll</Property>
				<Property Name="Destination[0].path" Type="Path">../NI_AB_PROJECTNAME.dll</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">..</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Dll_compatibilityWith2011" Type="Bool">false</Property>
				<Property Name="Dll_delayOSMsg" Type="Bool">true</Property>
				<Property Name="Dll_headerGUID" Type="Str">{B70EBD59-EE03-4F5B-A885-68B347A1C45A}</Property>
				<Property Name="Dll_includeTypeLibrary" Type="Bool">true</Property>
				<Property Name="Dll_libGUID" Type="Str">{EA8D270A-EC1E-4511-8137-BBCA8E7C84D1}</Property>
				<Property Name="Source[0].itemID" Type="Str">{A7B79704-F737-480F-A91A-96A6B4F5D77F}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].ExportedVI.VIProtoInfo[0]CallingConv" Type="Int">1</Property>
				<Property Name="Source[1].ExportedVI.VIProtoInfo[0]Name" Type="Str">AnalogIn_Create</Property>
				<Property Name="Source[1].ExportedVI.VIProtoInfo[0]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[1].ExportedVI.VIProtoInfo[0]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[1].ExportedVI.VIProtoInfo[0]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[1].ExportedVI.VIProtoInfo[0]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[1].ExportedVI.VIProtoInfo[0]VIProtoName" Type="Str">return value</Property>
				<Property Name="Source[1].ExportedVI.VIProtoInfo[0]VIProtoOutputIdx" Type="Int">0</Property>
				<Property Name="Source[1].ExportedVI.VIProtoInfo[0]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[1].ExportedVI.VIProtoInfoCPTM" Type="Bin">&amp;1#!!!!!!!)!$U!)!!B"&lt;G&amp;M&lt;W&gt;*&lt;A!!%A$Q!!%!!!-!!!!!!!E!!!!!!1!"</Property>
				<Property Name="Source[1].ExportedVI.VIProtoInfoVIProtoItemCount" Type="Int">1</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/OOUtil.lvlib/AnalogIn_Create.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[10].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[10].itemID" Type="Ref">/My Computer/OOUtil.lvlib/AnalogOut_getDACPins.vi</Property>
				<Property Name="Source[10].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[10].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[100].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[100].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getLastExceptionStackTrace.vi</Property>
				<Property Name="Source[100].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[100].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[101].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[101].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getMaximumIntegrationTime.vi</Property>
				<Property Name="Source[101].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[101].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[102].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[102].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getMaximumIntensity.vi</Property>
				<Property Name="Source[102].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[102].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[103].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[103].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getMinimumIntegrationTime.vi</Property>
				<Property Name="Source[103].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[103].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[104].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[104].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getName.vi</Property>
				<Property Name="Source[104].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[104].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[105].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[105].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getNumberOfDarkPixels.vi</Property>
				<Property Name="Source[105].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[105].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[106].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[106].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getNumberOfEnabledChannels.vi</Property>
				<Property Name="Source[106].type" Type="Str">VI</Property>
				<Property Name="Source[107].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[107].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getNumberOfPixels.vi</Property>
				<Property Name="Source[107].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[107].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[108].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[108].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getNumberOfSpectrometersFound.vi</Property>
				<Property Name="Source[108].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[108].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[109].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[109].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getScansToAverage.vi</Property>
				<Property Name="Source[109].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[109].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[11].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[11].itemID" Type="Ref">/My Computer/OOUtil.lvlib/AnalogOut_isDACPresent.vi</Property>
				<Property Name="Source[11].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[11].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[110].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[110].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getScansToAverage_1.vi</Property>
				<Property Name="Source[110].type" Type="Str">VI</Property>
				<Property Name="Source[111].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[111].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getSerialNumber.vi</Property>
				<Property Name="Source[111].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[111].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[112].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[112].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getSpectrum.vi</Property>
				<Property Name="Source[112].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[112].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[113].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[113].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getSpectrum_1.vi</Property>
				<Property Name="Source[113].type" Type="Str">VI</Property>
				<Property Name="Source[114].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[114].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getStrobeEnable.vi</Property>
				<Property Name="Source[114].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[114].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[115].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[115].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getStrobeEnable_1.vi</Property>
				<Property Name="Source[115].type" Type="Str">VI</Property>
				<Property Name="Source[116].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[116].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getWavelength.vi</Property>
				<Property Name="Source[116].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[116].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[117].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[117].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getWavelength_1.vi</Property>
				<Property Name="Source[117].type" Type="Str">VI</Property>
				<Property Name="Source[118].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[118].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getWavelengthFirst.vi</Property>
				<Property Name="Source[118].type" Type="Str">VI</Property>
				<Property Name="Source[119].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[119].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getWavelengthFirst_1.vi</Property>
				<Property Name="Source[119].type" Type="Str">VI</Property>
				<Property Name="Source[12].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[12].itemID" Type="Ref">/My Computer/OOUtil.lvlib/AnalogOut_setDACCounts.vi</Property>
				<Property Name="Source[12].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[12].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[120].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[120].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getWavelengthIntercept.vi</Property>
				<Property Name="Source[120].type" Type="Str">VI</Property>
				<Property Name="Source[121].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[121].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getWavelengthIntercept_1.vi</Property>
				<Property Name="Source[121].type" Type="Str">VI</Property>
				<Property Name="Source[122].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[122].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getWavelengths.vi</Property>
				<Property Name="Source[122].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[122].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[123].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[123].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getWavelengths_1.vi</Property>
				<Property Name="Source[123].type" Type="Str">VI</Property>
				<Property Name="Source[124].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[124].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getWavelengthSecond.vi</Property>
				<Property Name="Source[124].type" Type="Str">VI</Property>
				<Property Name="Source[125].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[125].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getWavelengthSecond_1.vi</Property>
				<Property Name="Source[125].type" Type="Str">VI</Property>
				<Property Name="Source[126].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[126].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getWavelengthThird.vi</Property>
				<Property Name="Source[126].type" Type="Str">VI</Property>
				<Property Name="Source[127].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[127].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getWavelengthThird_1.vi</Property>
				<Property Name="Source[127].type" Type="Str">VI</Property>
				<Property Name="Source[128].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[0]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[0]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[0]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[0]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[0]VIProtoName" Type="Str">return value</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[0]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[0]VIProtoPassBy" Type="Int">0</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[1]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[1]VIProtoInputIdx" Type="Int">3</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[1]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[1]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[1]VIProtoName" Type="Str">WrapperIN</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[1]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[1]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[2]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[2]VIProtoInputIdx" Type="Int">2</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[2]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[2]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[2]VIProtoName" Type="Str">SpectrometerIndex</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[2]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[2]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[3]CallingConv" Type="Int">1</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[3]Name" Type="Str">Wrapper_highSpdAcq_AllocateBuffer</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[3]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[3]VIProtoInputIdx" Type="Int">1</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[3]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[3]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[3]VIProtoName" Type="Str">numberOfSpectra</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[3]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfo[3]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfoCPTM" Type="Bin">&amp;1#!!!!!!!5!%5!)!!N8=G&amp;Q='6S)%^V&gt;!!81!-!%7ZV&lt;7*F=C"P:C"4='6D&gt;(*B!"F!"Q!35X"F9X2S&lt;WVF&gt;'6S)%FO:'6Y!!!21!A!#F&gt;S98"Q:8)A35Y!!#1!]!!%!!!!!1!#!!-$!!!A!!!.!Q!!#!!!!!A!!!!)!!!!!!%!"!</Property>
				<Property Name="Source[128].ExportedVI.VIProtoInfoVIProtoItemCount" Type="Int">4</Property>
				<Property Name="Source[128].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_highSpdAcq_AllocateBuffer.vi</Property>
				<Property Name="Source[128].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[128].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[129].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[129].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_highSpdAcq_GetNumberOfSpectraAcquired.vi</Property>
				<Property Name="Source[129].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[129].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[13].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[13].itemID" Type="Ref">/My Computer/OOUtil.lvlib/BoardTemperature_Create.vi</Property>
				<Property Name="Source[13].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[13].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[130].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[130].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_highSpdAcq_GetSpectrum.vi</Property>
				<Property Name="Source[130].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[130].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[131].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[131].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_highSpdAcq_GetTimeStamp.vi</Property>
				<Property Name="Source[131].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[131].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[132].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[132].ExportedVI.VIProtoInfo[0]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[132].ExportedVI.VIProtoInfo[0]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[132].ExportedVI.VIProtoInfo[0]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[132].ExportedVI.VIProtoInfo[0]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[132].ExportedVI.VIProtoInfo[0]VIProtoName" Type="Str">return value</Property>
				<Property Name="Source[132].ExportedVI.VIProtoInfo[0]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[132].ExportedVI.VIProtoInfo[0]VIProtoPassBy" Type="Int">0</Property>
				<Property Name="Source[132].ExportedVI.VIProtoInfo[1]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[132].ExportedVI.VIProtoInfo[1]VIProtoInputIdx" Type="Int">2</Property>
				<Property Name="Source[132].ExportedVI.VIProtoInfo[1]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[132].ExportedVI.VIProtoInfo[1]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[132].ExportedVI.VIProtoInfo[1]VIProtoName" Type="Str">WrapperIn</Property>
				<Property Name="Source[132].ExportedVI.VIProtoInfo[1]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[132].ExportedVI.VIProtoInfo[1]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[132].ExportedVI.VIProtoInfo[2]CallingConv" Type="Int">1</Property>
				<Property Name="Source[132].ExportedVI.VIProtoInfo[2]Name" Type="Str">Wrapper_highSpdAcq_StartAquisition</Property>
				<Property Name="Source[132].ExportedVI.VIProtoInfo[2]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[132].ExportedVI.VIProtoInfo[2]VIProtoInputIdx" Type="Int">1</Property>
				<Property Name="Source[132].ExportedVI.VIProtoInfo[2]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[132].ExportedVI.VIProtoInfo[2]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[132].ExportedVI.VIProtoInfo[2]VIProtoName" Type="Str">SpectrometerIndex</Property>
				<Property Name="Source[132].ExportedVI.VIProtoInfo[2]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[132].ExportedVI.VIProtoInfo[2]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[132].ExportedVI.VIProtoInfoCPTM" Type="Bin">&amp;1#!!!!!!!1!%5!)!!N8=G&amp;Q='6S)%^V&gt;!!:1!-!%F.Q:7.U=G^N:82F=C"*&lt;G2F?!!!%5!)!!J8=G&amp;Q='6S)%FO!!!?!0!!!Q!!!!%!!A-!!"!!!!U#!!!)!!!!#!!!!!!"!!-</Property>
				<Property Name="Source[132].ExportedVI.VIProtoInfoVIProtoItemCount" Type="Int">3</Property>
				<Property Name="Source[132].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_highSpdAcq_StartAquisition.vi</Property>
				<Property Name="Source[132].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[132].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[133].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[133].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_highSpdAcq_StartAquisition_1.vi</Property>
				<Property Name="Source[133].type" Type="Str">VI</Property>
				<Property Name="Source[134].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[134].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_hightSpdAcq_IsSaturated.vi</Property>
				<Property Name="Source[134].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[134].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[135].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[135].ExportedVI.VIProtoInfo[0]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[135].ExportedVI.VIProtoInfo[0]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[135].ExportedVI.VIProtoInfo[0]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[135].ExportedVI.VIProtoInfo[0]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[135].ExportedVI.VIProtoInfo[0]VIProtoName" Type="Str">return value</Property>
				<Property Name="Source[135].ExportedVI.VIProtoInfo[0]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[135].ExportedVI.VIProtoInfo[0]VIProtoPassBy" Type="Int">0</Property>
				<Property Name="Source[135].ExportedVI.VIProtoInfo[1]CallingConv" Type="Int">1</Property>
				<Property Name="Source[135].ExportedVI.VIProtoInfo[1]Name" Type="Str">Wrapper_hightSpdAcq_StopAcquisition</Property>
				<Property Name="Source[135].ExportedVI.VIProtoInfo[1]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[135].ExportedVI.VIProtoInfo[1]VIProtoInputIdx" Type="Int">1</Property>
				<Property Name="Source[135].ExportedVI.VIProtoInfo[1]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[135].ExportedVI.VIProtoInfo[1]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[135].ExportedVI.VIProtoInfo[1]VIProtoName" Type="Str">WrapperIn</Property>
				<Property Name="Source[135].ExportedVI.VIProtoInfo[1]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[135].ExportedVI.VIProtoInfo[1]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[135].ExportedVI.VIProtoInfoCPTM" Type="Bin">&amp;1#!!!!!!!-!%5!)!!N8=G&amp;Q='6S)%^V&gt;!!21!A!#F&gt;S98"Q:8)A37Y!!"A!]!!#!!!!!1-!!!A!!!U"!!!)!!!!!!%!!A</Property>
				<Property Name="Source[135].ExportedVI.VIProtoInfoVIProtoItemCount" Type="Int">2</Property>
				<Property Name="Source[135].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_hightSpdAcq_StopAcquisition.vi</Property>
				<Property Name="Source[135].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[135].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[136].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[136].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_insertKey.vi</Property>
				<Property Name="Source[136].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[136].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[137].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[137].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_isFeatureSupportedLS450.vi</Property>
				<Property Name="Source[137].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[137].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[138].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[138].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_isSaturated.vi</Property>
				<Property Name="Source[138].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[138].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[139].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[139].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_isSaturated_1.vi</Property>
				<Property Name="Source[139].type" Type="Str">VI</Property>
				<Property Name="Source[14].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[14].itemID" Type="Ref">/My Computer/OOUtil.lvlib/BoardTemperature_Destroy.vi</Property>
				<Property Name="Source[14].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[14].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[140].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[140].ExportedVI.VIProtoInfo[0]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[140].ExportedVI.VIProtoInfo[0]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[140].ExportedVI.VIProtoInfo[0]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[140].ExportedVI.VIProtoInfo[0]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[140].ExportedVI.VIProtoInfo[0]VIProtoName" Type="Str">return value</Property>
				<Property Name="Source[140].ExportedVI.VIProtoInfo[0]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[140].ExportedVI.VIProtoInfo[0]VIProtoPassBy" Type="Int">0</Property>
				<Property Name="Source[140].ExportedVI.VIProtoInfo[1]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[140].ExportedVI.VIProtoInfo[1]VIProtoInputIdx" Type="Int">0</Property>
				<Property Name="Source[140].ExportedVI.VIProtoInfo[1]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[140].ExportedVI.VIProtoInfo[1]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[140].ExportedVI.VIProtoInfo[1]VIProtoName" Type="Str">WrapperIn</Property>
				<Property Name="Source[140].ExportedVI.VIProtoInfo[1]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[140].ExportedVI.VIProtoInfo[1]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[140].ExportedVI.VIProtoInfo[2]CallingConv" Type="Int">1</Property>
				<Property Name="Source[140].ExportedVI.VIProtoInfo[2]Name" Type="Str">Wrapper_openAllSpectrometers</Property>
				<Property Name="Source[140].ExportedVI.VIProtoInfo[2]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[140].ExportedVI.VIProtoInfo[2]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[140].ExportedVI.VIProtoInfo[2]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[140].ExportedVI.VIProtoInfo[2]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[140].ExportedVI.VIProtoInfo[2]VIProtoName" Type="Str">NumberOfSpectrometers</Property>
				<Property Name="Source[140].ExportedVI.VIProtoInfo[2]VIProtoOutputIdx" Type="Int">1</Property>
				<Property Name="Source[140].ExportedVI.VIProtoInfo[2]VIProtoPassBy" Type="Int">0</Property>
				<Property Name="Source[140].ExportedVI.VIProtoInfoCPTM" Type="Bin">&amp;1#!!!!!!!1!%5!)!!J8=G&amp;Q='6S)%FO!!!&gt;1!-!&amp;UZV&lt;7*F=C"P:C"4='6D&gt;(*P&lt;76U:8*T!"&amp;!#!!,6X*B=("F=C"0&gt;81!(A$Q!!-!!!!"!!)$!!!3!!!)!!!!#1!!!!U!!!!!!1!$</Property>
				<Property Name="Source[140].ExportedVI.VIProtoInfoVIProtoItemCount" Type="Int">3</Property>
				<Property Name="Source[140].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_openAllSpectrometers.vi</Property>
				<Property Name="Source[140].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[140].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[141].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[141].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_openNetworkSpectrometer.vi</Property>
				<Property Name="Source[141].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[141].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[142].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[142].ExportedVI.VIProtoInfo[0]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[142].ExportedVI.VIProtoInfo[0]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[142].ExportedVI.VIProtoInfo[0]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[142].ExportedVI.VIProtoInfo[0]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[142].ExportedVI.VIProtoInfo[0]VIProtoName" Type="Str">return value</Property>
				<Property Name="Source[142].ExportedVI.VIProtoInfo[0]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[142].ExportedVI.VIProtoInfo[0]VIProtoPassBy" Type="Int">0</Property>
				<Property Name="Source[142].ExportedVI.VIProtoInfo[1]CallingConv" Type="Int">1</Property>
				<Property Name="Source[142].ExportedVI.VIProtoInfo[1]Name" Type="Str">Wrapper_removeKey</Property>
				<Property Name="Source[142].ExportedVI.VIProtoInfo[1]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[142].ExportedVI.VIProtoInfo[1]VIProtoInputIdx" Type="Int">1</Property>
				<Property Name="Source[142].ExportedVI.VIProtoInfo[1]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[142].ExportedVI.VIProtoInfo[1]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[142].ExportedVI.VIProtoInfo[1]VIProtoName" Type="Str">WrapperIn</Property>
				<Property Name="Source[142].ExportedVI.VIProtoInfo[1]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[142].ExportedVI.VIProtoInfo[1]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[142].ExportedVI.VIProtoInfoCPTM" Type="Bin">&amp;1#!!!!!!!-!%5!)!!N8=G&amp;Q='6S)%^V&gt;!!21!A!#F&gt;S98"Q:8)A37Y!!"A!]!!#!!!!!1-!!!A!!!U"!!!)!!!!!!%!!A</Property>
				<Property Name="Source[142].ExportedVI.VIProtoInfoVIProtoItemCount" Type="Int">2</Property>
				<Property Name="Source[142].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_removeKey.vi</Property>
				<Property Name="Source[142].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[142].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[143].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[0]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[0]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[0]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[0]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[0]VIProtoName" Type="Str">return value</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[0]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[0]VIProtoPassBy" Type="Int">0</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[1]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[1]VIProtoInputIdx" Type="Int">3</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[1]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[1]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[1]VIProtoName" Type="Str">WrapperIn</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[1]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[1]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[2]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[2]VIProtoInputIdx" Type="Int">2</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[2]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[2]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[2]VIProtoName" Type="Str">Index</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[2]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[2]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[3]CallingConv" Type="Int">1</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[3]Name" Type="Str">Wrapper_setAutoToggleStrobeLampEnable</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[3]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[3]VIProtoInputIdx" Type="Int">1</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[3]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[3]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[3]VIProtoName" Type="Str">Enable</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[3]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfo[3]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfoCPTM" Type="Bin">&amp;1#!!!!!!!5!%5!)!!N8=G&amp;Q='6S)%^V&gt;!!.1!5!"E6O97*M:1!!#U!$!!6*&lt;G2F?!!01!A!#6&gt;S98"Q:8**&lt;A!E!0!!"!!!!!%!!A!$!Q!!)!!!$1-!!!A!!!!)!!!!#!!!!!!"!!1</Property>
				<Property Name="Source[143].ExportedVI.VIProtoInfoVIProtoItemCount" Type="Int">4</Property>
				<Property Name="Source[143].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_setAutoToggleStrobeLampEnable.vi</Property>
				<Property Name="Source[143].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[143].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[144].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[144].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_setAutoToggleStrobeLampEnable_1.vi</Property>
				<Property Name="Source[144].type" Type="Str">VI</Property>
				<Property Name="Source[145].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[0]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[0]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[0]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[0]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[0]VIProtoName" Type="Str">return value</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[0]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[0]VIProtoPassBy" Type="Int">0</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[1]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[1]VIProtoInputIdx" Type="Int">3</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[1]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[1]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[1]VIProtoName" Type="Str">WrapperIn</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[1]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[1]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[2]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[2]VIProtoInputIdx" Type="Int">2</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[2]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[2]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[2]VIProtoName" Type="Str">Index</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[2]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[2]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[3]CallingConv" Type="Int">1</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[3]Name" Type="Str">Wrapper_setBoxcarWidth</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[3]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[3]VIProtoInputIdx" Type="Int">1</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[3]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[3]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[3]VIProtoName" Type="Str">BoxcarWidth</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[3]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfo[3]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfoCPTM" Type="Bin">&amp;1#!!!!!!!5!%5!)!!N8=G&amp;Q='6S)%^V&gt;!!41!-!$%*P?'.B=C"8;72U;!!!#U!$!!6*&lt;G2F?!!21!A!#F&gt;S98"Q:8)A37Y!!#1!]!!%!!!!!1!#!!-$!!!A!!!.!Q!!#!!!!!A!!!!)!!!!!!%!"!</Property>
				<Property Name="Source[145].ExportedVI.VIProtoInfoVIProtoItemCount" Type="Int">4</Property>
				<Property Name="Source[145].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_setBoxcarWidth.vi</Property>
				<Property Name="Source[145].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[145].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[146].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[146].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_setBoxcarWidth_1.vi</Property>
				<Property Name="Source[146].type" Type="Str">VI</Property>
				<Property Name="Source[147].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[0]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[0]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[0]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[0]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[0]VIProtoName" Type="Str">return value</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[0]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[0]VIProtoPassBy" Type="Int">0</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[1]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[1]VIProtoInputIdx" Type="Int">3</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[1]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[1]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[1]VIProtoName" Type="Str">WrapperIn</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[1]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[1]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[2]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[2]VIProtoInputIdx" Type="Int">2</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[2]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[2]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[2]VIProtoName" Type="Str">Index</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[2]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[2]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[3]CallingConv" Type="Int">1</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[3]Name" Type="Str">Wrapper_setCorrectForDetectorNonlinearity</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[3]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[3]VIProtoInputIdx" Type="Int">1</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[3]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[3]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[3]VIProtoName" Type="Str">OnOff</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[3]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfo[3]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfoCPTM" Type="Bin">&amp;1#!!!!!!!5!%5!)!!N8=G&amp;Q='6S)%^V&gt;!!.1!-!"E^O,U^G:A!!#U!$!!6*&lt;G2F?!!21!A!#F&gt;S98"Q:8)A37Y!!#1!]!!%!!!!!1!#!!-$!!!A!!!.!Q!!#!!!!!A!!!!)!!!!!!%!"!</Property>
				<Property Name="Source[147].ExportedVI.VIProtoInfoVIProtoItemCount" Type="Int">4</Property>
				<Property Name="Source[147].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_setCorrectForDetectorNonlinearity.vi</Property>
				<Property Name="Source[147].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[147].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[148].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[148].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_setCorrectForDetectorNonlinearity_1.vi</Property>
				<Property Name="Source[148].type" Type="Str">VI</Property>
				<Property Name="Source[149].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[0]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[0]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[0]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[0]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[0]VIProtoName" Type="Str">return value</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[0]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[0]VIProtoPassBy" Type="Int">0</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[1]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[1]VIProtoInputIdx" Type="Int">3</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[1]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[1]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[1]VIProtoName" Type="Str">WrapperIn</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[1]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[1]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[2]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[2]VIProtoInputIdx" Type="Int">2</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[2]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[2]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[2]VIProtoName" Type="Str">Index</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[2]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[2]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[3]CallingConv" Type="Int">1</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[3]Name" Type="Str">Wrapper_setCorrectForElectricalDark</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[3]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[3]VIProtoInputIdx" Type="Int">1</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[3]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[3]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[3]VIProtoName" Type="Str">OnOff</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[3]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfo[3]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfoCPTM" Type="Bin">&amp;1#!!!!!!!5!%5!)!!N8=G&amp;Q='6S)%^V&gt;!!.1!-!"E^O,U^G:A!!#U!$!!6*&lt;G2F?!!21!A!#F&gt;S98"Q:8)A37Y!!#1!]!!%!!!!!1!#!!-$!!!A!!!.!Q!!#!!!!!A!!!!)!!!!!!%!"!</Property>
				<Property Name="Source[149].ExportedVI.VIProtoInfoVIProtoItemCount" Type="Int">4</Property>
				<Property Name="Source[149].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_setCorrectForElectricalDark.vi</Property>
				<Property Name="Source[149].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[149].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[15].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[15].itemID" Type="Ref">/My Computer/OOUtil.lvlib/BoardTemperature_getBoardTemperatureCelsius.vi</Property>
				<Property Name="Source[15].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[15].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[150].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[150].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_setCorrectForElectricalDark_1.vi</Property>
				<Property Name="Source[150].type" Type="Str">VI</Property>
				<Property Name="Source[151].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[151].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_setEEPromInfo.vi</Property>
				<Property Name="Source[151].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[151].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[152].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[0]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[0]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[0]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[0]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[0]VIProtoName" Type="Str">return value</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[0]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[0]VIProtoPassBy" Type="Int">0</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[1]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[1]VIProtoInputIdx" Type="Int">3</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[1]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[1]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[1]VIProtoName" Type="Str">WrapperIn</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[1]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[1]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[2]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[2]VIProtoInputIdx" Type="Int">2</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[2]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[2]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[2]VIProtoName" Type="Str">Index</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[2]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[2]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[3]CallingConv" Type="Int">1</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[3]Name" Type="Str">Wrapper_setExternalTriggerMode</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[3]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[3]VIProtoInputIdx" Type="Int">1</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[3]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[3]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[3]VIProtoName" Type="Str">TriggerMode</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[3]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfo[3]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfoCPTM" Type="Bin">&amp;1#!!!!!!!5!%5!)!!N8=G&amp;Q='6S)%^V&gt;!!41!-!$&amp;2S;7&gt;H:8)A47^E:1!!#U!$!!6*&lt;G2F?!!21!A!#F&gt;S98"Q:8)A37Y!!#1!]!!%!!!!!1!#!!-$!!!A!!!.!Q!!#!!!!!A!!!!)!!!!!!%!"!</Property>
				<Property Name="Source[152].ExportedVI.VIProtoInfoVIProtoItemCount" Type="Int">4</Property>
				<Property Name="Source[152].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_setExternalTriggerMode.vi</Property>
				<Property Name="Source[152].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[152].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[153].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[153].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_setExternalTriggerMode_1.vi</Property>
				<Property Name="Source[153].type" Type="Str">VI</Property>
				<Property Name="Source[154].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[0]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[0]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[0]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[0]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[0]VIProtoName" Type="Str">return value</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[0]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[0]VIProtoPassBy" Type="Int">0</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[1]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[1]VIProtoInputIdx" Type="Int">3</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[1]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[1]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[1]VIProtoName" Type="Str">WrapperIn</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[1]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[1]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[2]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[2]VIProtoInputIdx" Type="Int">2</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[2]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[2]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[2]VIProtoName" Type="Str">Index</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[2]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[2]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[3]CallingConv" Type="Int">1</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[3]Name" Type="Str">Wrapper_setIntegrationTime</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[3]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[3]VIProtoInputIdx" Type="Int">1</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[3]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[3]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[3]VIProtoName" Type="Str">IntegrationTime</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[3]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfo[3]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfoCPTM" Type="Bin">&amp;1#!!!!!!!5!%5!)!!N8=G&amp;Q='6S)%^V&gt;!!81!-!%%FO&gt;'6H=G&amp;U;7^O)&amp;2J&lt;75!!!N!!Q!&amp;37ZE:8A!%5!)!!J8=G&amp;Q='6S)%FO!!!E!0!!"!!!!!%!!A!$!Q!!)!!!$1-!!!A!!!!)!!!!#!!!!!!"!!1</Property>
				<Property Name="Source[154].ExportedVI.VIProtoInfoVIProtoItemCount" Type="Int">4</Property>
				<Property Name="Source[154].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_setIntegrationTime.vi</Property>
				<Property Name="Source[154].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[154].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[155].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[155].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_setIntegrationTime_1.vi</Property>
				<Property Name="Source[155].type" Type="Str">VI</Property>
				<Property Name="Source[156].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[0]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[0]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[0]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[0]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[0]VIProtoName" Type="Str">return value</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[0]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[0]VIProtoPassBy" Type="Int">0</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[1]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[1]VIProtoInputIdx" Type="Int">3</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[1]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[1]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[1]VIProtoName" Type="Str">WrapperIn</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[1]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[1]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[2]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[2]VIProtoInputIdx" Type="Int">2</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[2]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[2]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[2]VIProtoName" Type="Str">Index</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[2]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[2]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[3]CallingConv" Type="Int">1</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[3]Name" Type="Str">Wrapper_setScansToAverage</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[3]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[3]VIProtoInputIdx" Type="Int">1</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[3]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[3]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[3]VIProtoName" Type="Str">Average</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[3]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfo[3]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfoCPTM" Type="Bin">&amp;1#!!!!!!!5!%5!)!!N8=G&amp;Q='6S)%^V&gt;!!.1!-!"U&amp;W:8*B:W5!#U!$!!6*&lt;G2F?!!21!A!#F&gt;S98"Q:8)A37Y!!#1!]!!%!!!!!1!#!!-$!!!A!!!.!Q!!#!!!!!A!!!!)!!!!!!%!"!</Property>
				<Property Name="Source[156].ExportedVI.VIProtoInfoVIProtoItemCount" Type="Int">4</Property>
				<Property Name="Source[156].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_setScansToAverage.vi</Property>
				<Property Name="Source[156].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[156].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[157].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[157].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_setScansToAverage_1.vi</Property>
				<Property Name="Source[157].type" Type="Str">VI</Property>
				<Property Name="Source[158].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[0]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[0]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[0]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[0]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[0]VIProtoName" Type="Str">return value</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[0]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[0]VIProtoPassBy" Type="Int">0</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[1]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[1]VIProtoInputIdx" Type="Int">3</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[1]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[1]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[1]VIProtoName" Type="Str">WrapperIn</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[1]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[1]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[2]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[2]VIProtoInputIdx" Type="Int">2</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[2]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[2]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[2]VIProtoName" Type="Str">Index</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[2]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[2]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[3]CallingConv" Type="Int">1</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[3]Name" Type="Str">Wrapper_setStrobeEnable</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[3]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[3]VIProtoInputIdx" Type="Int">1</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[3]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[3]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[3]VIProtoName" Type="Str">OnOff</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[3]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfo[3]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfoCPTM" Type="Bin">&amp;1#!!!!!!!5!%5!)!!N8=G&amp;Q='6S)%^V&gt;!!.1!-!"E^O,U^G:A!!#U!$!!6*&lt;G2F?!!21!A!#F&gt;S98"Q:8)A37Y!!#1!]!!%!!!!!1!#!!-$!!!A!!!.!Q!!#!!!!!A!!!!)!!!!!!%!"!</Property>
				<Property Name="Source[158].ExportedVI.VIProtoInfoVIProtoItemCount" Type="Int">4</Property>
				<Property Name="Source[158].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_setStrobeEnable.vi</Property>
				<Property Name="Source[158].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[158].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[159].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[159].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_setStrobeEnable_1.vi</Property>
				<Property Name="Source[159].type" Type="Str">VI</Property>
				<Property Name="Source[16].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[16].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ContinuousStrobe_continuousStrobeCountsToMicros.vi</Property>
				<Property Name="Source[16].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[16].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[160].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[160].ExportedVI.VIProtoInfo[0]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[160].ExportedVI.VIProtoInfo[0]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[160].ExportedVI.VIProtoInfo[0]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[160].ExportedVI.VIProtoInfo[0]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[160].ExportedVI.VIProtoInfo[0]VIProtoName" Type="Str">return value</Property>
				<Property Name="Source[160].ExportedVI.VIProtoInfo[0]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[160].ExportedVI.VIProtoInfo[0]VIProtoPassBy" Type="Int">0</Property>
				<Property Name="Source[160].ExportedVI.VIProtoInfo[1]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[160].ExportedVI.VIProtoInfo[1]VIProtoInputIdx" Type="Int">2</Property>
				<Property Name="Source[160].ExportedVI.VIProtoInfo[1]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[160].ExportedVI.VIProtoInfo[1]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[160].ExportedVI.VIProtoInfo[1]VIProtoName" Type="Str">WrapperIn</Property>
				<Property Name="Source[160].ExportedVI.VIProtoInfo[1]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[160].ExportedVI.VIProtoInfo[1]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[160].ExportedVI.VIProtoInfo[2]CallingConv" Type="Int">1</Property>
				<Property Name="Source[160].ExportedVI.VIProtoInfo[2]Name" Type="Str">Wrapper_stopAveraging</Property>
				<Property Name="Source[160].ExportedVI.VIProtoInfo[2]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[160].ExportedVI.VIProtoInfo[2]VIProtoInputIdx" Type="Int">1</Property>
				<Property Name="Source[160].ExportedVI.VIProtoInfo[2]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[160].ExportedVI.VIProtoInfo[2]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[160].ExportedVI.VIProtoInfo[2]VIProtoName" Type="Str">SpectrometerIndex</Property>
				<Property Name="Source[160].ExportedVI.VIProtoInfo[2]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[160].ExportedVI.VIProtoInfo[2]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[160].ExportedVI.VIProtoInfoCPTM" Type="Bin">&amp;1#!!!!!!!1!%5!)!!N8=G&amp;Q='6S)%^V&gt;!!:1!-!%F.Q:7.U=G^N:82F=C"*&lt;G2F?!!!%5!)!!J8=G&amp;Q='6S)%FO!!!?!0!!!Q!!!!%!!A-!!"!!!!U#!!!)!!!!#!!!!!!"!!-</Property>
				<Property Name="Source[160].ExportedVI.VIProtoInfoVIProtoItemCount" Type="Int">3</Property>
				<Property Name="Source[160].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_stopAveraging.vi</Property>
				<Property Name="Source[160].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[160].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[161].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[161].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_stopAveraging_1.vi</Property>
				<Property Name="Source[161].type" Type="Str">VI</Property>
				<Property Name="Source[17].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[17].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ContinuousStrobe_Create.vi</Property>
				<Property Name="Source[17].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[17].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[18].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[18].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ContinuousStrobe_Destroy.vi</Property>
				<Property Name="Source[18].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[18].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[19].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[19].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ContinuousStrobe_getContinuousStrobeDelayIncrement.vi</Property>
				<Property Name="Source[19].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[19].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[2].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[2].ExportedVI.VIProtoInfo[0]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[2].ExportedVI.VIProtoInfo[0]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[2].ExportedVI.VIProtoInfo[0]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[2].ExportedVI.VIProtoInfo[0]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[2].ExportedVI.VIProtoInfo[0]VIProtoName" Type="Str">return value</Property>
				<Property Name="Source[2].ExportedVI.VIProtoInfo[0]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[2].ExportedVI.VIProtoInfo[0]VIProtoPassBy" Type="Int">0</Property>
				<Property Name="Source[2].ExportedVI.VIProtoInfo[1]CallingConv" Type="Int">1</Property>
				<Property Name="Source[2].ExportedVI.VIProtoInfo[1]Name" Type="Str">AnalogIn_Destroy</Property>
				<Property Name="Source[2].ExportedVI.VIProtoInfo[1]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[2].ExportedVI.VIProtoInfo[1]VIProtoInputIdx" Type="Int">0</Property>
				<Property Name="Source[2].ExportedVI.VIProtoInfo[1]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[2].ExportedVI.VIProtoInfo[1]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[2].ExportedVI.VIProtoInfo[1]VIProtoName" Type="Str">AnalogIn</Property>
				<Property Name="Source[2].ExportedVI.VIProtoInfo[1]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[2].ExportedVI.VIProtoInfo[1]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[2].ExportedVI.VIProtoInfoCPTM" Type="Bin">&amp;1#!!!!!!!)!$U!)!!B"&lt;G&amp;M&lt;W&gt;*&lt;A!!%A$Q!!%!!!-!!!!!!!A!!!!!!1!"</Property>
				<Property Name="Source[2].ExportedVI.VIProtoInfoVIProtoItemCount" Type="Int">2</Property>
				<Property Name="Source[2].itemID" Type="Ref">/My Computer/OOUtil.lvlib/AnalogIn_Destroy.vi</Property>
				<Property Name="Source[2].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[2].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[20].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[20].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ContinuousStrobe_getContinuousStrobeDelayMaximum.vi</Property>
				<Property Name="Source[20].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[20].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[21].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[21].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ContinuousStrobe_getContinuousStrobeDelayMinimum.vi</Property>
				<Property Name="Source[21].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[21].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[22].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[22].ExportedVI.VIProtoInfo[0]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[22].ExportedVI.VIProtoInfo[0]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[22].ExportedVI.VIProtoInfo[0]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[22].ExportedVI.VIProtoInfo[0]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[22].ExportedVI.VIProtoInfo[0]VIProtoName" Type="Str">return value</Property>
				<Property Name="Source[22].ExportedVI.VIProtoInfo[0]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[22].ExportedVI.VIProtoInfo[0]VIProtoPassBy" Type="Int">0</Property>
				<Property Name="Source[22].ExportedVI.VIProtoInfo[1]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[22].ExportedVI.VIProtoInfo[1]VIProtoInputIdx" Type="Int">2</Property>
				<Property Name="Source[22].ExportedVI.VIProtoInfo[1]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[22].ExportedVI.VIProtoInfo[1]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[22].ExportedVI.VIProtoInfo[1]VIProtoName" Type="Str">ContinuousStrobeIn</Property>
				<Property Name="Source[22].ExportedVI.VIProtoInfo[1]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[22].ExportedVI.VIProtoInfo[1]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[22].ExportedVI.VIProtoInfo[2]CallingConv" Type="Int">1</Property>
				<Property Name="Source[22].ExportedVI.VIProtoInfo[2]Name" Type="Str">ContinuousStrobe_setContinuousStrobeDelay</Property>
				<Property Name="Source[22].ExportedVI.VIProtoInfo[2]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[22].ExportedVI.VIProtoInfo[2]VIProtoInputIdx" Type="Int">1</Property>
				<Property Name="Source[22].ExportedVI.VIProtoInfo[2]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[22].ExportedVI.VIProtoInfo[2]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[22].ExportedVI.VIProtoInfo[2]VIProtoName" Type="Str">delay</Property>
				<Property Name="Source[22].ExportedVI.VIProtoInfo[2]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[22].ExportedVI.VIProtoInfo[2]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[22].ExportedVI.VIProtoInfoCPTM" Type="Bin">&amp;1#!!!!!!!1!'U!)!"2$&lt;WZU;7ZV&lt;X6T5X2S&lt;W*F)%^V&gt;!!!#U!$!!6E:7RB?1!:1!A!%U.P&lt;H2J&lt;H6P&gt;8.4&gt;(*P9G5A37Y!(A$Q!!-!!!!"!!)$!!!1!!!.!A!!#!!!!!A!!!!!!1!$</Property>
				<Property Name="Source[22].ExportedVI.VIProtoInfoVIProtoItemCount" Type="Int">3</Property>
				<Property Name="Source[22].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ContinuousStrobe_setContinuousStrobeDelay.vi</Property>
				<Property Name="Source[22].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[22].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[23].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[23].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ExternalTriggerDelay_Create.vi</Property>
				<Property Name="Source[23].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[23].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[24].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[24].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ExternalTriggerDelay_Destroy.vi</Property>
				<Property Name="Source[24].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[24].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[25].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[25].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ExternalTriggerDelay_getExternalTriggerDelayIncrement.vi</Property>
				<Property Name="Source[25].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[25].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[26].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[26].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ExternalTriggerDelay_getExternalTriggerDelayMaximum.vi</Property>
				<Property Name="Source[26].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[26].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[27].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[27].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ExternalTriggerDelay_getExternalTriggerDelayMinimum.vi</Property>
				<Property Name="Source[27].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[27].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[28].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[28].ExportedVI.VIProtoInfo[0]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[28].ExportedVI.VIProtoInfo[0]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[28].ExportedVI.VIProtoInfo[0]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[28].ExportedVI.VIProtoInfo[0]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[28].ExportedVI.VIProtoInfo[0]VIProtoName" Type="Str">return value</Property>
				<Property Name="Source[28].ExportedVI.VIProtoInfo[0]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[28].ExportedVI.VIProtoInfo[0]VIProtoPassBy" Type="Int">0</Property>
				<Property Name="Source[28].ExportedVI.VIProtoInfo[1]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[28].ExportedVI.VIProtoInfo[1]VIProtoInputIdx" Type="Int">2</Property>
				<Property Name="Source[28].ExportedVI.VIProtoInfo[1]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[28].ExportedVI.VIProtoInfo[1]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[28].ExportedVI.VIProtoInfo[1]VIProtoName" Type="Str">ExternalTriggerDelayIn</Property>
				<Property Name="Source[28].ExportedVI.VIProtoInfo[1]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[28].ExportedVI.VIProtoInfo[1]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[28].ExportedVI.VIProtoInfo[2]CallingConv" Type="Int">1</Property>
				<Property Name="Source[28].ExportedVI.VIProtoInfo[2]Name" Type="Str">ExternalTriggerDelay_setExternalTriggerDelay</Property>
				<Property Name="Source[28].ExportedVI.VIProtoInfo[2]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[28].ExportedVI.VIProtoInfo[2]VIProtoInputIdx" Type="Int">1</Property>
				<Property Name="Source[28].ExportedVI.VIProtoInfo[2]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[28].ExportedVI.VIProtoInfo[2]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[28].ExportedVI.VIProtoInfo[2]VIProtoName" Type="Str">microseconds</Property>
				<Property Name="Source[28].ExportedVI.VIProtoInfo[2]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[28].ExportedVI.VIProtoInfo[2]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[28].ExportedVI.VIProtoInfoCPTM" Type="Bin">&amp;1#!!!!!!!1!(U!)!"B&amp;?(2F=GZB&lt;&amp;2S;7&gt;H:8*%:7RB?3"0&gt;81!!".!!Q!-&lt;7FD=G^T:7.P&lt;G2T!!!&gt;1!A!&amp;U6Y&gt;'6S&lt;G&amp;M6(*J:W&gt;F=E2F&lt;'&amp;Z)%FO!"Y!]!!$!!!!!1!#!Q!!%!!!$1)!!!A!!!!)!!!!!!%!!Q</Property>
				<Property Name="Source[28].ExportedVI.VIProtoInfoVIProtoItemCount" Type="Int">3</Property>
				<Property Name="Source[28].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ExternalTriggerDelay_setExternalTriggerDelay.vi</Property>
				<Property Name="Source[28].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[28].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[29].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[29].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ExternalTriggerDelay_triggerDelayCountsToMicroseconds.vi</Property>
				<Property Name="Source[29].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[29].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[3].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[3].ExportedVI.VIProtoInfo[0]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[3].ExportedVI.VIProtoInfo[0]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[3].ExportedVI.VIProtoInfo[0]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[3].ExportedVI.VIProtoInfo[0]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[3].ExportedVI.VIProtoInfo[0]VIProtoName" Type="Str">return value</Property>
				<Property Name="Source[3].ExportedVI.VIProtoInfo[0]VIProtoOutputIdx" Type="Int">0</Property>
				<Property Name="Source[3].ExportedVI.VIProtoInfo[0]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[3].ExportedVI.VIProtoInfo[1]CallingConv" Type="Int">1</Property>
				<Property Name="Source[3].ExportedVI.VIProtoInfo[1]Name" Type="Str">AnalogIn_getVoltageIn</Property>
				<Property Name="Source[3].ExportedVI.VIProtoInfo[1]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[3].ExportedVI.VIProtoInfo[1]VIProtoInputIdx" Type="Int">1</Property>
				<Property Name="Source[3].ExportedVI.VIProtoInfo[1]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[3].ExportedVI.VIProtoInfo[1]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[3].ExportedVI.VIProtoInfo[1]VIProtoName" Type="Str">AnalogIn</Property>
				<Property Name="Source[3].ExportedVI.VIProtoInfo[1]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[3].ExportedVI.VIProtoInfo[1]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[3].ExportedVI.VIProtoInfoCPTM" Type="Bin">&amp;1#!!!!!!!-!$5!+!!&gt;7&lt;WRU97&gt;F!!^!#!!)17ZB&lt;'^H37Y!!"A!]!!#!!!!!1-!!!A!!!E!!!!)!!!!!!%!!A</Property>
				<Property Name="Source[3].ExportedVI.VIProtoInfoVIProtoItemCount" Type="Int">2</Property>
				<Property Name="Source[3].itemID" Type="Ref">/My Computer/OOUtil.lvlib/AnalogIn_getVoltageIn.vi</Property>
				<Property Name="Source[3].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[3].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[30].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[30].itemID" Type="Ref">/My Computer/OOUtil.lvlib/GPIO_Create.vi</Property>
				<Property Name="Source[30].type" Type="Str">VI</Property>
				<Property Name="Source[31].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[31].itemID" Type="Ref">/My Computer/OOUtil.lvlib/GPIO_Destroy.vi</Property>
				<Property Name="Source[31].type" Type="Str">VI</Property>
				<Property Name="Source[32].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[32].itemID" Type="Ref">/My Computer/OOUtil.lvlib/GPIO_getDirectionBits.vi</Property>
				<Property Name="Source[32].type" Type="Str">VI</Property>
				<Property Name="Source[33].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[33].itemID" Type="Ref">/My Computer/OOUtil.lvlib/GPIO_getMuxBits.vi</Property>
				<Property Name="Source[33].type" Type="Str">VI</Property>
				<Property Name="Source[34].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[34].itemID" Type="Ref">/My Computer/OOUtil.lvlib/GPIO_getNumberOfPins.vi</Property>
				<Property Name="Source[34].type" Type="Str">VI</Property>
				<Property Name="Source[35].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[35].itemID" Type="Ref">/My Computer/OOUtil.lvlib/GPIO_getTotalGPIOBits.vi</Property>
				<Property Name="Source[35].type" Type="Str">VI</Property>
				<Property Name="Source[36].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[36].itemID" Type="Ref">/My Computer/OOUtil.lvlib/GPIO_getValueBit.vi</Property>
				<Property Name="Source[36].type" Type="Str">VI</Property>
				<Property Name="Source[37].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[37].itemID" Type="Ref">/My Computer/OOUtil.lvlib/GPIO_getValueBits.vi</Property>
				<Property Name="Source[37].type" Type="Str">VI</Property>
				<Property Name="Source[38].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[38].itemID" Type="Ref">/My Computer/OOUtil.lvlib/GPIO_setDirectionBit.vi</Property>
				<Property Name="Source[38].type" Type="Str">VI</Property>
				<Property Name="Source[39].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[39].itemID" Type="Ref">/My Computer/OOUtil.lvlib/GPIO_setDirectionBitmask.vi</Property>
				<Property Name="Source[39].type" Type="Str">VI</Property>
				<Property Name="Source[4].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[4].itemID" Type="Ref">/My Computer/OOUtil.lvlib/AnalogOut_analogoutCountsToVolts.vi</Property>
				<Property Name="Source[4].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[4].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[40].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[40].itemID" Type="Ref">/My Computer/OOUtil.lvlib/GPIO_setMuxBit.vi</Property>
				<Property Name="Source[40].type" Type="Str">VI</Property>
				<Property Name="Source[41].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[41].itemID" Type="Ref">/My Computer/OOUtil.lvlib/GPIO_setMuxBitsmask.vi</Property>
				<Property Name="Source[41].type" Type="Str">VI</Property>
				<Property Name="Source[42].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[42].itemID" Type="Ref">/My Computer/OOUtil.lvlib/GPIO_setValueBit.vi</Property>
				<Property Name="Source[42].type" Type="Str">VI</Property>
				<Property Name="Source[43].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[43].itemID" Type="Ref">/My Computer/OOUtil.lvlib/GPIO_setValueBitmask.vi</Property>
				<Property Name="Source[43].type" Type="Str">VI</Property>
				<Property Name="Source[44].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[44].itemID" Type="Ref">/My Computer/OOUtil.lvlib/SingleStrobe_Create.vi</Property>
				<Property Name="Source[44].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[44].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[45].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[45].itemID" Type="Ref">/My Computer/OOUtil.lvlib/SingleStrobe_Destroy.vi</Property>
				<Property Name="Source[45].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[45].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[46].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[46].itemID" Type="Ref">/My Computer/OOUtil.lvlib/SingleStrobe_getSingleStrobeCountsToMicros.vi</Property>
				<Property Name="Source[46].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[46].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[47].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[47].itemID" Type="Ref">/My Computer/OOUtil.lvlib/SingleStrobe_getSingleStrobeHigh.vi</Property>
				<Property Name="Source[47].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[47].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[48].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[48].itemID" Type="Ref">/My Computer/OOUtil.lvlib/SingleStrobe_getSingleStrobeIncrement.vi</Property>
				<Property Name="Source[48].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[48].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[49].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[49].itemID" Type="Ref">/My Computer/OOUtil.lvlib/SingleStrobe_getSingleStrobeLow.vi</Property>
				<Property Name="Source[49].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[49].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[5].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[5].itemID" Type="Ref">/My Computer/OOUtil.lvlib/AnalogOut_Create.vi</Property>
				<Property Name="Source[5].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[5].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[50].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[50].itemID" Type="Ref">/My Computer/OOUtil.lvlib/SingleStrobe_getSingleStrobeMaximum.vi</Property>
				<Property Name="Source[50].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[50].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[51].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[51].itemID" Type="Ref">/My Computer/OOUtil.lvlib/SingleStrobe_getSingleStrobeMinimum.vi</Property>
				<Property Name="Source[51].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[51].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[52].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[52].ExportedVI.VIProtoInfo[0]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[52].ExportedVI.VIProtoInfo[0]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[52].ExportedVI.VIProtoInfo[0]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[52].ExportedVI.VIProtoInfo[0]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[52].ExportedVI.VIProtoInfo[0]VIProtoName" Type="Str">return value</Property>
				<Property Name="Source[52].ExportedVI.VIProtoInfo[0]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[52].ExportedVI.VIProtoInfo[0]VIProtoPassBy" Type="Int">0</Property>
				<Property Name="Source[52].ExportedVI.VIProtoInfo[1]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[52].ExportedVI.VIProtoInfo[1]VIProtoInputIdx" Type="Int">2</Property>
				<Property Name="Source[52].ExportedVI.VIProtoInfo[1]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[52].ExportedVI.VIProtoInfo[1]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[52].ExportedVI.VIProtoInfo[1]VIProtoName" Type="Str">SingleStrobeIn</Property>
				<Property Name="Source[52].ExportedVI.VIProtoInfo[1]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[52].ExportedVI.VIProtoInfo[1]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[52].ExportedVI.VIProtoInfo[2]CallingConv" Type="Int">1</Property>
				<Property Name="Source[52].ExportedVI.VIProtoInfo[2]Name" Type="Str">SingleStrobe_setSingleStrobeHigh</Property>
				<Property Name="Source[52].ExportedVI.VIProtoInfo[2]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[52].ExportedVI.VIProtoInfo[2]VIProtoInputIdx" Type="Int">1</Property>
				<Property Name="Source[52].ExportedVI.VIProtoInfo[2]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[52].ExportedVI.VIProtoInfo[2]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[52].ExportedVI.VIProtoInfo[2]VIProtoName" Type="Str">SingleStrobeHigh</Property>
				<Property Name="Source[52].ExportedVI.VIProtoInfo[2]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[52].ExportedVI.VIProtoInfo[2]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[52].ExportedVI.VIProtoInfoCPTM" Type="Bin">&amp;1#!!!!!!!1!&amp;U!)!""4;7ZH&lt;'64&gt;(*P9G5A4X6U!!!81!-!%6.J&lt;G&gt;M:6.U=G^C:3");7&gt;I!"6!#!!05WFO:WRF5X2S&lt;W*F)%FO!"Y!]!!$!!!!!1!#!Q!!%!!!$1)!!!A!!!!)!!!!!!%!!Q</Property>
				<Property Name="Source[52].ExportedVI.VIProtoInfoVIProtoItemCount" Type="Int">3</Property>
				<Property Name="Source[52].itemID" Type="Ref">/My Computer/OOUtil.lvlib/SingleStrobe_setSingleStrobeHigh.vi</Property>
				<Property Name="Source[52].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[52].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[53].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[53].ExportedVI.VIProtoInfo[0]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[53].ExportedVI.VIProtoInfo[0]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[53].ExportedVI.VIProtoInfo[0]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[53].ExportedVI.VIProtoInfo[0]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[53].ExportedVI.VIProtoInfo[0]VIProtoName" Type="Str">return value</Property>
				<Property Name="Source[53].ExportedVI.VIProtoInfo[0]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[53].ExportedVI.VIProtoInfo[0]VIProtoPassBy" Type="Int">0</Property>
				<Property Name="Source[53].ExportedVI.VIProtoInfo[1]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[53].ExportedVI.VIProtoInfo[1]VIProtoInputIdx" Type="Int">2</Property>
				<Property Name="Source[53].ExportedVI.VIProtoInfo[1]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[53].ExportedVI.VIProtoInfo[1]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[53].ExportedVI.VIProtoInfo[1]VIProtoName" Type="Str">SingleStrobeIn</Property>
				<Property Name="Source[53].ExportedVI.VIProtoInfo[1]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[53].ExportedVI.VIProtoInfo[1]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[53].ExportedVI.VIProtoInfo[2]CallingConv" Type="Int">1</Property>
				<Property Name="Source[53].ExportedVI.VIProtoInfo[2]Name" Type="Str">SingleStrobe_setSingleStrobeLow</Property>
				<Property Name="Source[53].ExportedVI.VIProtoInfo[2]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[53].ExportedVI.VIProtoInfo[2]VIProtoInputIdx" Type="Int">1</Property>
				<Property Name="Source[53].ExportedVI.VIProtoInfo[2]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[53].ExportedVI.VIProtoInfo[2]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[53].ExportedVI.VIProtoInfo[2]VIProtoName" Type="Str">SingleStrobeLow</Property>
				<Property Name="Source[53].ExportedVI.VIProtoInfo[2]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[53].ExportedVI.VIProtoInfo[2]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[53].ExportedVI.VIProtoInfoCPTM" Type="Bin">&amp;1#!!!!!!!1!&amp;U!)!""4;7ZH&lt;'64&gt;(*P9G5A4X6U!!!81!-!%6.J&lt;G&gt;M:3"4&gt;(*P9G5A4'^X!"6!#!!05WFO:WRF5X2S&lt;W*F)%FO!"Y!]!!$!!!!!1!#!Q!!%!!!$1)!!!A!!!!)!!!!!!%!!Q</Property>
				<Property Name="Source[53].ExportedVI.VIProtoInfoVIProtoItemCount" Type="Int">3</Property>
				<Property Name="Source[53].itemID" Type="Ref">/My Computer/OOUtil.lvlib/SingleStrobe_setSingleStrobeLow.vi</Property>
				<Property Name="Source[53].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[53].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[54].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[54].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ThermoElectric_Create.vi</Property>
				<Property Name="Source[54].type" Type="Str">VI</Property>
				<Property Name="Source[55].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[55].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ThermoElectric_Destroy.vi</Property>
				<Property Name="Source[55].type" Type="Str">VI</Property>
				<Property Name="Source[56].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[56].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ThermoElectric_getDetectorTemperatureCelsius.vi</Property>
				<Property Name="Source[56].type" Type="Str">VI</Property>
				<Property Name="Source[57].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[57].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ThermoElectric_getDetectorTemperatureSetPointCelsius.vi</Property>
				<Property Name="Source[57].type" Type="Str">VI</Property>
				<Property Name="Source[58].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[58].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ThermoElectric_getSetPointIncrementCelsius.vi</Property>
				<Property Name="Source[58].type" Type="Str">VI</Property>
				<Property Name="Source[59].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[59].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ThermoElectric_getSetPointMaximumCelsius.vi</Property>
				<Property Name="Source[59].type" Type="Str">VI</Property>
				<Property Name="Source[6].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[6].itemID" Type="Ref">/My Computer/OOUtil.lvlib/AnalogOut_Destroy.vi</Property>
				<Property Name="Source[6].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[6].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[60].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[60].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ThermoElectric_getSetPointMinimumCelsius.vi</Property>
				<Property Name="Source[60].type" Type="Str">VI</Property>
				<Property Name="Source[61].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[61].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ThermoElectric_isSaveTECEnabled.vi</Property>
				<Property Name="Source[61].type" Type="Str">VI</Property>
				<Property Name="Source[62].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[62].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ThermoElectric_saveTECState.vi</Property>
				<Property Name="Source[62].type" Type="Str">VI</Property>
				<Property Name="Source[63].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[63].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ThermoElectric_setDetectorSetPointCelcius.vi</Property>
				<Property Name="Source[63].type" Type="Str">VI</Property>
				<Property Name="Source[64].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[64].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ThermoElectric_setDetectorSetPointCelsiusInt.vi</Property>
				<Property Name="Source[64].type" Type="Str">VI</Property>
				<Property Name="Source[65].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[65].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ThermoElectric_setFanEnable.vi</Property>
				<Property Name="Source[65].type" Type="Str">VI</Property>
				<Property Name="Source[66].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[66].itemID" Type="Ref">/My Computer/OOUtil.lvlib/ThermoElectric_setTECEnable.vi</Property>
				<Property Name="Source[66].type" Type="Str">VI</Property>
				<Property Name="Source[67].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[67].ExportedVI.VIProtoInfo[0]VIProtoDir" Type="Int">1</Property>
				<Property Name="Source[67].ExportedVI.VIProtoInfo[0]VIProtoInputIdx" Type="Int">-1</Property>
				<Property Name="Source[67].ExportedVI.VIProtoInfo[0]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[67].ExportedVI.VIProtoInfo[0]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[67].ExportedVI.VIProtoInfo[0]VIProtoName" Type="Str">return value</Property>
				<Property Name="Source[67].ExportedVI.VIProtoInfo[0]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[67].ExportedVI.VIProtoInfo[0]VIProtoPassBy" Type="Int">0</Property>
				<Property Name="Source[67].ExportedVI.VIProtoInfo[1]CallingConv" Type="Int">1</Property>
				<Property Name="Source[67].ExportedVI.VIProtoInfo[1]Name" Type="Str">Wrapper_closeAllSpectrometers</Property>
				<Property Name="Source[67].ExportedVI.VIProtoInfo[1]VIProtoDir" Type="Int">0</Property>
				<Property Name="Source[67].ExportedVI.VIProtoInfo[1]VIProtoInputIdx" Type="Int">1</Property>
				<Property Name="Source[67].ExportedVI.VIProtoInfo[1]VIProtoLenInput" Type="Int">-1</Property>
				<Property Name="Source[67].ExportedVI.VIProtoInfo[1]VIProtoLenOutput" Type="Int">-1</Property>
				<Property Name="Source[67].ExportedVI.VIProtoInfo[1]VIProtoName" Type="Str">WrapperIn</Property>
				<Property Name="Source[67].ExportedVI.VIProtoInfo[1]VIProtoOutputIdx" Type="Int">-1</Property>
				<Property Name="Source[67].ExportedVI.VIProtoInfo[1]VIProtoPassBy" Type="Int">1</Property>
				<Property Name="Source[67].ExportedVI.VIProtoInfoCPTM" Type="Bin">&amp;1#!!!!!!!-!%5!)!!N8=G&amp;Q='6S)%^V&gt;!!21!A!#F&gt;S98"Q:8)A37Y!!"A!]!!#!!!!!1-!!!A!!!U"!!!)!!!!!!%!!A</Property>
				<Property Name="Source[67].ExportedVI.VIProtoInfoVIProtoItemCount" Type="Int">2</Property>
				<Property Name="Source[67].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_closeAllSpectrometers.vi</Property>
				<Property Name="Source[67].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[67].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[68].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[68].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_closeSpectrometer.vi</Property>
				<Property Name="Source[68].type" Type="Str">VI</Property>
				<Property Name="Source[69].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[69].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_closeSpetrometer.vi</Property>
				<Property Name="Source[69].type" Type="Str">VI</Property>
				<Property Name="Source[7].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[7].itemID" Type="Ref">/My Computer/OOUtil.lvlib/AnalogOut_getDACIncrement.vi</Property>
				<Property Name="Source[7].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[7].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[70].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[70].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_Create.vi</Property>
				<Property Name="Source[70].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[70].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[71].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[71].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_Destroy.vi</Property>
				<Property Name="Source[71].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[71].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[72].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[72].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_exportToGramsSPC.vi</Property>
				<Property Name="Source[72].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[72].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[73].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[73].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_exportToGramsSPC_1.vi</Property>
				<Property Name="Source[73].type" Type="Str">VI</Property>
				<Property Name="Source[74].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[74].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getApiVersion.vi</Property>
				<Property Name="Source[74].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[74].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[75].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[75].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getBench.vi</Property>
				<Property Name="Source[75].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[75].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[76].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[76].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getBoxcarWidth.vi</Property>
				<Property Name="Source[76].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[76].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[77].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[77].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getBoxcarWidth_1.vi</Property>
				<Property Name="Source[77].type" Type="Str">VI</Property>
				<Property Name="Source[78].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[78].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getBuildNumber.vi</Property>
				<Property Name="Source[78].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[78].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[79].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[79].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getExternalTriggerMode.vi</Property>
				<Property Name="Source[79].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[79].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[8].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[8].itemID" Type="Ref">/My Computer/OOUtil.lvlib/AnalogOut_getDACMaximum.vi</Property>
				<Property Name="Source[8].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[8].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[80].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[80].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getExternalTriggerMode_1.vi</Property>
				<Property Name="Source[80].type" Type="Str">VI</Property>
				<Property Name="Source[81].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[81].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getFeatureControllerAnalogIn.vi</Property>
				<Property Name="Source[81].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[81].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[82].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[82].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getFeatureControllerAnalogOut.vi</Property>
				<Property Name="Source[82].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[82].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[83].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[83].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getFeatureControllerBoardTemperature.vi</Property>
				<Property Name="Source[83].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[83].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[84].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[84].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getFeatureControllerContinuousStrobe.vi</Property>
				<Property Name="Source[84].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[84].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[85].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[85].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getFeatureControllerExternalTriggerDelay.vi</Property>
				<Property Name="Source[85].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[85].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[86].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[86].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getFeatureControllerGPIO.vi</Property>
				<Property Name="Source[86].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[86].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[87].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[87].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getFeatureControllerIrradianceCalibrationFactor.vi</Property>
				<Property Name="Source[87].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[87].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[88].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[88].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getFeatureControllerLS450.vi</Property>
				<Property Name="Source[88].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[88].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[89].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[89].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getFeatureControllerNonlinearityCorrectionProvider.vi</Property>
				<Property Name="Source[89].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[89].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[9].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[9].itemID" Type="Ref">/My Computer/OOUtil.lvlib/AnalogOut_getDACMinimum.vi</Property>
				<Property Name="Source[9].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[9].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[90].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[90].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getFeatureControllerSingleStrobe.vi</Property>
				<Property Name="Source[90].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[90].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[91].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[91].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getFeatureControllerSPIBus.vi</Property>
				<Property Name="Source[91].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[91].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[92].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[92].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getFeatureControllerStrayLightCorrection.vi</Property>
				<Property Name="Source[92].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[92].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[93].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[93].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getFeatureControllerThermoElectric.vi</Property>
				<Property Name="Source[93].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[93].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[94].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[94].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getFeatureControllerVersion.vi</Property>
				<Property Name="Source[94].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[94].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[95].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[95].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getFeatureControllerWavelengthCalibraionProvider.vi</Property>
				<Property Name="Source[95].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[95].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[96].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[96].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getFirmwareVersion.vi</Property>
				<Property Name="Source[96].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[96].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[97].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[97].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getIntegrationTime.vi</Property>
				<Property Name="Source[97].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[97].type" Type="Str">ExportedVI</Property>
				<Property Name="Source[98].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[98].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getIntegrationTime_1.vi</Property>
				<Property Name="Source[98].type" Type="Str">VI</Property>
				<Property Name="Source[99].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[99].itemID" Type="Ref">/My Computer/OOUtil.lvlib/Wrapper_getLastException.vi</Property>
				<Property Name="Source[99].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[99].type" Type="Str">ExportedVI</Property>
				<Property Name="SourceCount" Type="Int">162</Property>
				<Property Name="TgtF_fileDescription" Type="Str">OOUtil</Property>
				<Property Name="TgtF_internalName" Type="Str">OOUtil</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2016 </Property>
				<Property Name="TgtF_productName" Type="Str">OOUtil</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{ACB32D46-1C17-45FE-AF0E-225697280983}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">OOUtil.dll</Property>
			</Item>
		</Item>
	</Item>
</Project>
