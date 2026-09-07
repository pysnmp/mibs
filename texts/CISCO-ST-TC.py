#
# PySNMP MIB module CISCO-ST-TC (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ST-TC
# Source digest sha256:4bc67ba781dda29c83b93e6f29bb1d9aff848fe5ed7f9db7bcd96db99f8fc0d0
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoModules, = mibBuilder.importSymbols("CISCO-SMI", "ciscoModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
storageTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 12, 4))
storageTextualConventions.setRevisions(('2021-02-12 00:00', '2016-11-30 00:00', '2012-08-08 00:00', '2011-07-26 00:00', '2010-12-24 00:00', '2008-05-16 00:00', '2005-12-17 00:00', '2004-05-18 00:00', '2003-09-26 00:00', '2003-08-07 00:00', '2002-10-04 00:00', '2002-09-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: storageTextualConventions.setRevisionsDescriptions(('Added enumerated values sixtyFourG and\n        autoMaxSixtyFourG to fcIfSpeed', 'Added enumerated values thirtyTwoG(12) and\n        autoMaxThirtyTwoG(13) to fcIfSpeed', 'Added sixteenG and automaxSixteenG in fcIfSpeed', '-Added following enum to FcIfSpeed:\n        autoMaxEightG.', '-Added following enums to FcIfSpeed:\n        autoMax4G, eightG and tenG.', '-Added following enums to FcPortTypes\n        TEXTUAL CONVENTION\n        npPort, tfPort, tnpPort\n        -Added following enums to InterfaceOperMode \n        TEXTUAL CONVENTION.\n        npPort, tfPort, tnpPort\n        -Added following enums to FcPortModuleTypes\n        TEXTUAL CONVENTION\n        sfpDwdm, qsfp, x2Dwdm\n        - Updated the description of the following objects:\n        FcPortTxTypes,\n        FcNameId.', '- Added following TCs\n        FcIfSfpDiagLevelType \n        FcIfServiceStateType\n        - Added following enums in FcPortModuleTypes\n        xfp, x2Short, x2Medium, x2Tall, xpakShort, \n        xpakMedium, xpakTall and xenpak. \n        - Added following enums in FcPortTxTypes. \n        tenGigBaseSr, tenGigBaseLr, tenGigBaseEr, \n        tenGigBaseLx4, tenGigBaseSw, tenGigBaseLw, \n        tenGigBaseEw. \n        - Added following enums in FcIfSpeed \n        fourG and autoMaxTwoG.', "Added new textual convention 'InterfaceOperMode'.", 'Obtained the OID for this MIB.', 'Added stPort(15) to FcPortTypes.', 'Added fvPort and portOperDown to FcPortTypes.\n        Added FcAddress and FcAddressType.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: storageTextualConventions.setLastUpdated('2021-02-12 00:00')
if mibBuilder.loadTexts: storageTextualConventions.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: storageTextualConventions.setContactInfo('Cisco Systems\n            Customer Service\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n            Tel: +1 800 553 -NETS\n            E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: storageTextualConventions.setDescription('This module defines textual conventions used in\n        Storage Area Network technology specific mibs.')
class VsanIndex(TextualConvention, Integer32):
    description = 'The VSAN id of a VSAN which uniquely identifies\n        a VSAN within a fabric. VSAN id is 12-bit \n        wide; so theoretically, 4096 VSANs can be defined in \n        a fabric and this device can be part of. However, VSAN \n        numbers 0 , 4094 and 4095 are reserved.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

class DomainId(TextualConvention, Integer32):
    description = 'The Domain Id of the switch. This is assigned\n        dynamically if the Domain Manager is enabled on \n        the switch or could be configured statically by \n        the user.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 239)

class DomainIdOrZero(TextualConvention, Integer32):
    description = "The Textual convention is an extension to\n        textual convetion 'DomainId'. It includes \n        the value '0'in addition the range 1-239.\n        Value '0' indicates that Domain Id has  \n        been neither configured nor assigned."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 239)

class FcAddressId(TextualConvention, OctetString):
    description = 'Represents Fibre Channel Address ID, a 24-bit\n        value unique within the address space of a Fabric.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class FcNameId(TextualConvention, OctetString):
    reference = 'Fibre Channel Framing and Signaling (FC-FS) Rev 1.70\n               - Section 14 Name_Indentifier Formats.'
    description = 'Represents the World Wide Name (WWN) associated with\n        a Fibre Channel (FC) entity. A WWN is a 64 bit address\n        to uniquely identify each entity within a Fibre Channel\n        fabric.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class FcNameIdOrZero(TextualConvention, OctetString):
    description = 'The World Wide Name (WWN) associated with a Fibre Channel\n        (FC) entity.  WWNs were initially defined as 64-bits in\n        length.  The latest definition (for future use) is 128-bits\n        long.  The zero-length string value is used in circumstances\n        where the WWN is unassigned/unknown.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), )
class FcClassOfServices(TextualConvention, Bits):
    description = 'Represents the class of service capability of an\n        NxPort or FxPort.'
    status = 'current'
    namedValues = NamedValues(("classF", 0), ("class1", 1), ("class2", 2), ("class3", 3), ("class4", 4), ("class5", 5), ("class6", 6))

class FcPortTypes(TextualConvention, Integer32):
    description = "Represents fibre channel port types:\n        auto (1)   - Mode is determined by port initialization \n                    scheme.\n        fPort (2)  - Fibre channel fabric port. \n        flPort (3) - Fibre channel arbitrated loop port.\n        ePort (4)  - Fabric Expansion port.\n        bPort (5)  - Bridging port.\n        fxPort (6) - This port can only be f_port or fl_port.\n        sdPort (7) - SPAN destination port. SD_ports transmit \n                    traffic copied from one or more source ports\n                    for monitoring purposes.        \n        tlPort (8) - Translation loop port.\n        nPort (9)   - Fibre channel N port.\n        nlPort (10) - Fibre channel NL port.\n        nxPort (11) - This port can only be n_port or nl_port.\n\n          -- read only port types.\n        tePort (12) - Trunking e_port.\n                     Note: A port which is administratively set\n                     to 'ePort', will operationally have type\n                     'tePort' if fcIfOperTrunkMode has the value\n                     'trunk'.\n        fvPort (13) - Virtual Port.\n        portOperDown (14) - port operationally down\n                            If a port is operationally down, the\n                            port mode is unknown. In such cases\n                            the operational port mode is shown \n                            as 'portOperDown'. \n        stPort (15) - SPAN Tunnel destination port.\n        npPort (16) - N Proxy port mode applicable only to N-port\n                      Virtualizer (NPV)\n        tfPort (17) - Trunking fibre channel fabric port.\n        tnpPort (18) - Trunking N Proxy port mode applicable only\n                      to N-port Virtualizer (NPV)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("auto", 1), ("fPort", 2), ("flPort", 3), ("ePort", 4), ("bPort", 5), ("fxPort", 6), ("sdPort", 7), ("tlPort", 8), ("nPort", 9), ("nlPort", 10), ("nxPort", 11), ("tePort", 12), ("fvPort", 13), ("portOperDown", 14), ("stPort", 15), ("npPort", 16), ("tfPort", 17), ("tnpPort", 18))

class FcPortTxTypes(TextualConvention, Integer32):
    reference = 'IEEE Std 802.3-2005 carrier sense multiple access \n        with collision detection (CSMA/CD) access method \n        and physical layer specification.'
    description = 'Represents port transciever technology types.\n        unknown (1) - unknown\n        longWaveLaser (2) - 1550nm laser\n        shortWaveLaser (3) - 850nm laser\n        longWaveLaserCostReduced (4) - 1310nm laser\n        electrical (5) - electrical \n        tenGigBaseSr (6)  - 10GBASE-SR 850nm laser\n        tenGigBaseLr (7)  - 10GBASE-LR 1310nm laser\n        tenGigBaseEr (8)  - 10GBASE-ER 1550nm laser\n        tenGigBaseLx4 (9) - 10GBASE-LX4 WWDM 1300nm laser\n        tenGigBaseSw (10)  - 850nm laser\n        tenGigBaseLw (11) - 1310nm laser\n        tenGigBaseEw (12) - 1550nm laser\n        .'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("unknown", 1), ("longWaveLaser", 2), ("shortWaveLaser", 3), ("longWaveLaserCostReduced", 4), ("electrical", 5), ("tenGigBaseSr", 6), ("tenGigBaseLr", 7), ("tenGigBaseEr", 8), ("tenGigBaseLx4", 9), ("tenGigBaseSw", 10), ("tenGigBaseLw", 11), ("tenGigBaseEw", 12))

class FcPortModuleTypes(TextualConvention, Integer32):
    description = 'Represents module type of the port connector. This\n        object refers to the hardware implementation of the port.\n        The enums are defined as per FC-GS-4 standard.\n        unknown             (1) - unknown\n        other               (2) - other\n        gbic                (3) - gbic (gigabit interface card)\n        embedded            (4) - gbic is part of the line card \n                                  and is unremovable\n        glm                 (5) - if its a gigabit link module \n                                  (GLM). A GLM has a different \n                                  form factor than GBIC. GLM is \n                                  not supported by our switch.\n        gbicWithSerialID    (6) - If GBIC serial id can be read\n        gbicWithoutSerialID (7) - If GBIC serial id cannot be read\n        sfpWithSerialID     (8) - If small form factor (SFP) \n                                  pluggable GBICs serial id can \n                                  be read\n        sfpWithoutSerialID  (9) - If small form factor (SFP) \n                                  pluggable GBICs serial id \n                                  cannot be read\n        The following enums are module types for 10 gigabit small \n        form factor pluggable sfp port connectors.\n        xfp                (10) - xfp \n        x2Short            (11) - x2 short \n        x2Medium           (12) - x2 medium\n        x2Tall             (13) - x2 tall\n        xpakShort          (14) - xpak short\n        xpakMedium         (15) - xpak medium\n        xpakTall           (16) - xpak tall\n        xenpak             (17) - xenpak\n        sfpDwdm            (18) - DWDM SFP type\n        qsfp               (19) - Quad small form-factor (QSFP) \n                                                          pluggable type\n        x2Dwdm             (20) - x2 DWDM\n        .'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("gbic", 3), ("embedded", 4), ("glm", 5), ("gbicWithSerialID", 6), ("gbicWithoutSerialID", 7), ("sfpWithSerialID", 8), ("sfpWithoutSerialID", 9), ("xfp", 10), ("x2Short", 11), ("x2Medium", 12), ("x2Tall", 13), ("xpakShort", 14), ("xpakMedium", 15), ("xpakTall", 16), ("xenpak", 17), ("sfpDwdm", 18), ("qsfp", 19), ("x2Dwdm", 20))

class FcIfSpeed(TextualConvention, Integer32):
    description = 'Represents the speed of a fibre channel port.\n        Following are the meanings of the enumerated values:\n          auto      (1) - Negotiate to determine the speed \n                          automatically.\n          oneG      (2) - 1Gbit \n          twoG      (3) - 2Gbit\n          fourG     (4) - 4Gbit \n          autoMaxTwoG (5)  - Negotiate to determine the \n                             speed automatically upto a \n                             maximum of 2Gbit.\n          eightG    (6) - 8Gbit\n          autoMaxFourG (7) - Negotiate to determine the\n                             speed automatically upto a\n                             maximum of 4Gbit.          \n          tenG      (8) - 10GBit.\n          autoMaxEightG (9) - Negotiate to determine the\n                             speed automatically upto a\n                             maximum of 8Gbit.\n          sixteenG  (10) - 16GBit.\n          autoMaxSixteenG (11) - Negotiate to determine the\n                             speed automatically upto a\n                             maximum of 16Gbit.\n          thirtyTwoG  (12) - 32GBit.\n          autoMaxThirtyTwoG (13) - Negotiate to determine the\n                             speed automatically upto a\n                             maximum of 32Gbit.\n          sixtyFourG  (14) - 64GBit.\n          autoMaxSixtyFourG (15) - Negotiate to determine the\n                             speed automatically upto a\n                             maximum of 64Gbit.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("auto", 1), ("oneG", 2), ("twoG", 3), ("fourG", 4), ("autoMaxTwoG", 5), ("eightG", 6), ("autoMaxFourG", 7), ("tenG", 8), ("autoMaxEightG", 9), ("sixteenG", 10), ("autoMaxSixteenG", 11), ("thirtyTwoG", 12), ("autoMaxThirtyTwoG", 13), ("sixtyFourG", 14), ("autoMaxSixtyFourG", 15))

class PortMemberList(TextualConvention, OctetString):
    description = "A list of ifIndex's of the ports that are members of\n        this list.\n\n        The value of this object is a concatenation of zero or\n        more 4-octet strings, where each 4-octet string contains\n        a 32-bit ifIndex value in network byte order.\n\n        A zero length string value means this list has no\n        members."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class FcAddress(TextualConvention, OctetString):
    description = 'Represents either the Fibre Channel Address ID or\n        the World Wide Name associated with a Fibre\n        Channel (FC) Entity.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(3, 3), ValueSizeConstraint(8, 8), )
class FcAddressType(TextualConvention, Integer32):
    description = 'Denotes if a Fibre Channel Address is\n        a World Wide Name (WWN) or a Fibre\n        Channel Address ID (FCID).\n        wwn(1) - address is WWN.\n        fcid(2) - address is FCID.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("wwn", 1), ("fcid", 2))

class InterfaceOperMode(TextualConvention, Integer32):
    description = "Represents the operational mode of an interface\n        auto (1) - Mode is determined by port initialization\n                   scheme.\n        fPort (2) - Fibre channel fabric port.\n        flPort (3) - Fibre channel arbitrated loop port.\n        ePort (4)  - Fabric Expansion port.\n        bPort (5)  - Bridging port.\n        fxPort (6) - This port can only be f_port or fl_port.\n        sdPort (7) - SPAN destination port. SD_ports transmit\n                     traffic copied from one or more source\n                     ports for monitoring purposes.\n        tlPort (8) - Translation loop port.\n        nPort (9)   - Fibre channel N port.\n        nlPort (10) - Fibre channel NL port.\n        nxPort (11) - This port can only be n_port or nl_port.\n\n        -- read only port types.\n        tePort (12) - Trunking e_port.\n                  Note: A port which is administratively set\n                  to 'ePort', will operationally have type\n                  'tePort' if fcIfOperTrunkMode has the value\n                  'trunk'.\n        fvPort (13) - Virtual Port.\n        portOperDown (14) - port operationally down\n                          If a port is operationally down, the\n                          port mode is unknown. In such cases\n                          the operational port mode is shown\n                          as 'portOperDown'.\n        stPort (15) - SPAN Tunnel destination port.\n        mgmtPort(16) - Mgmt Port.\n        ipsPort(17) - Ethernet Port.\n        evPort(18) - FCIP tunnels on Ethernet ports.\n        npPort (19) - N Proxy port mode applicable only \n                      to N-port Virtualizer (NPV).\n        tfPort (20) - Trunking fibre channel fabric port.\n        tnpPort (21) - Trunking N Proxy port mode applicable only\n                              to N-port Virtualizer (NPV)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21))
    namedValues = NamedValues(("auto", 1), ("fPort", 2), ("flPort", 3), ("ePort", 4), ("bPort", 5), ("fxPort", 6), ("sdPort", 7), ("tlPort", 8), ("nPort", 9), ("nlPort", 10), ("nxPort", 11), ("tePort", 12), ("fvPort", 13), ("portOperDown", 14), ("stPort", 15), ("mgmtPort", 16), ("ipsPort", 17), ("evPort", 18), ("npPort", 19), ("tfPort", 20), ("tnpPort", 21))

class FcIfServiceStateType(TextualConvention, Integer32):
    description = 'Represents the service state of a Fibre Channel\n        interface. Following are the meanings of the \n        enumerated values:\n\n        inService    (1) - interface is in service and is\n                      allowed to become operational.\n        outOfService (2) - interface is removed from service \n                      and is not allowed to become \n                      operational.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("inService", 1), ("outOfService", 2))

class FcIfSfpDiagLevelType(TextualConvention, Integer32):
    description = 'Represents the severity level of the SFP\n        diagnostic information of an interface for \n        temperature, voltage, current, optical \n        transmit and receive power.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 1), ("normal", 2), ("lowWarning", 3), ("lowAlarm", 4), ("highWarning", 5), ("highAlarm", 6))

mibBuilder.exportSymbols("CISCO-ST-TC", DomainId=DomainId, DomainIdOrZero=DomainIdOrZero, FcAddress=FcAddress, FcAddressId=FcAddressId, FcAddressType=FcAddressType, FcClassOfServices=FcClassOfServices, FcIfServiceStateType=FcIfServiceStateType, FcIfSfpDiagLevelType=FcIfSfpDiagLevelType, FcIfSpeed=FcIfSpeed, FcNameId=FcNameId, FcNameIdOrZero=FcNameIdOrZero, FcPortModuleTypes=FcPortModuleTypes, FcPortTxTypes=FcPortTxTypes, FcPortTypes=FcPortTypes, InterfaceOperMode=InterfaceOperMode, PYSNMP_MODULE_ID=storageTextualConventions, PortMemberList=PortMemberList, VsanIndex=VsanIndex, storageTextualConventions=storageTextualConventions)
