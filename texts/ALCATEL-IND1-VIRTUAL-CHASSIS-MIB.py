#
# PySNMP MIB module ALCATEL-IND1-VIRTUAL-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nokia/aos7/ALCATEL-IND1-VIRTUAL-CHASSIS-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 17:15:06 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
softentIND1VirtualChassisManager, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1VirtualChassisManager")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, ModuleIdentity, Counter64, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Integer32, Gauge32, Counter32, NotificationType, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Counter64", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Integer32", "Gauge32", "Counter32", "NotificationType", "Unsigned32", "Bits")
RowStatus, MacAddress, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "MacAddress", "TruthValue", "TextualConvention", "DisplayString")
alcatelIND1VirtualChassisMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1))
alcatelIND1VirtualChassisMIB.setRevisions(('2011-05-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIB.setRevisionsDescriptions(('Addressing discrepancies with Alcatel Standard.',))
if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIB.setLastUpdated('201105250000Z')
if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIB.setOrganization('Alcatel-Lucent, Enterprise Solutions Division')
if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIB.setContactInfo('Please consult with Customer Service to ensure the most appropriate\n      version of this document is used with the products in question:\n\n                 Alcatel-Lucent, Enterprise Solutions Division\n                (Formerly Alcatel Internetworking, Incorporated)\n                        26801 West Agoura Road\n                     Agoura Hills, CA  91301-5122\n                       United States Of America\n\n     Telephone:               North America  +1 800 995 2696\n                              Latin America  +1 877 919 9526\n                              Europe         +31 23 556 0100\n                              Asia           +65 394 7933\n                              All Other      +1 818 878 4507\n\n     Electronic Mail:         support@ind.alcatel.com\n     World Wide Web:          http://alcatel-lucent.com/wps/portal/enterprise\n     File Transfer Protocol:  ftp://ftp.ind.alcatel.com/pub/products/mibs')
if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIB.setDescription('This module describes an authoritative enterprise-specific Simple\n        etwork Management Protocol (SNMP) Management Information Base (MIB):\n\n        For the Birds Of Prey Product Line, this is the Chassis Supervision\n        Chassis MIB\n        for managing physical chassis objects not covered in the IETF\n        Entity MIB (rfc 2737).\n\n        The right to make changes in specification and other information\n        contained in this document without prior notice is reserved.\n\n        No liability shall be assumed for any incidental, indirect, special, or\n        consequential damages whatsoever arising from or related to this\n        document or the information contained herein.\n\n        Vendors, end-users, and other interested parties are granted\n        non-exclusive license to use this specification in connection with\n        management of the products for which it is intended to be used.\n\n                   Copyright (C) 1995-2007 Alcatel-Lucent\n                       ALL RIGHTS RESERVED WORLDWIDE')
alcatelIND1VirtualChassisMIBNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 0))
if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIBNotifications.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIBNotifications.setDescription('Branch For Virtual-Chassis manager MIB\n            Subsystem Managed Objects.')
alcatelIND1VirtualChassisMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1))
if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIBObjects.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIBObjects.setDescription('Branch For Virtual-Chassis manager MIB\n            Subsystem Managed Objects.')
alcatelIND1VirtualChassisMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2))
if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIBConformance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIBConformance.setDescription('Branch For Chassis Supervision Virtual Chassis MIB\n            Subsystem Conformance Information.')
alcatelIND1VirtualChassisMIBVCSP = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3))
if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIBVCSP.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIBVCSP.setDescription('Branch for VC Split Protection.')
alcatelIND1VirtualChassisMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIBGroups.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIBGroups.setDescription('Branch For Chassis Supervision Virtual Chassis MIB\n            Subsystem Units Of Conformance.')
alcatelIND1VirtualChassisMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIBCompliances.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIBCompliances.setDescription('Branch For Chassis Supervision Virtual Chassis MIB\n            Subsystem Compliance Statements.')
class VirtualOperChassisId(TextualConvention, Integer32):
    description = 'Chassis identifier globally unique within a virtual-chassis domain,\n                 which is a set of chassis configured to operate together\n                 providing virtual-chassis services. When the value of this object\n                 is equal to 0, the chassis operates in stand-alone mode; otherwise,\n                 the chassis is capable of operating in a virtual-chassis system.\n                 This chassis ID is defined as following to do configuration.\n                 Standalone mode or boot up:\n                          (0) local chassis configuraiton\n                 VC mode: (0) all chassis configuration Note: this is not valid for get case\n                          (1..6) this indicates chassis id of virtual-chassis mode\n                          (101..) this indicates a chassis with duplicated chassis id status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class VirtualConfigChassisId(TextualConvention, Integer32):
    description = 'This is a configuraion for chassis id.\n                 (0) if no chassis id been applied\n                 (1..6) configure VC valid chassis id'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 6)

class VirtualChassisHelloInterval(TextualConvention, Integer32):
    description = 'Time interval, in seconds, at which hello messages will be sent to the peer.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class VirtualChassisControlVlan(TextualConvention, Integer32):
    description = 'Virtual Chassis control vlan.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(2, 4094)

class VirtualChassisCmmSlot(TextualConvention, Integer32):
    description = 'CMM slot indicator.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 65, 66))
    namedValues = NamedValues(("notPresent", 0), ("cmmSlot1", 65), ("cmmSlot2", 66))

class VirtualChassisNiSlot(TextualConvention, Integer32):
    description = 'NI slot indicator.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 8)

class VirtualChassisVflId(TextualConvention, Integer32):
    description = 'Virtual Fabric Link Id.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

class VirtualChassisConsistency(TextualConvention, Integer32):
    description = 'Virtual-chassis parameter consistency status with master chassis. \n                         inconsis(0): able to compare with master chassis but not consistent \n                         consis(1): able to compare with master chassis and consistent\n                         na(2): not able to compare with master chassis since virtual-chassis is not connected yet  \n                         disabeled(3):  not able to compare with master because of standalone mode'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("inconsistent", 0), ("consistent", 1), ("na", 2), ("disabled", 3))

class VirtualChassisRole(TextualConvention, Integer32):
    description = 'Virtual-chassis chassis role: \n                         unassigned(0): init chassis role and election not complete yet\n                         master(1): indicate chasis is in master role after election\n                         slave(2): indicate chasis is in slave role after election\n                         inconsistent(3): indicate chassis is not consistent after election\n                         startuperror(4): chassis unable to start in virtual-chassis mode'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unassigned", 0), ("master", 1), ("slave", 2), ("inconsistent", 3), ("startuperror", 4))

class VirtualChassisStatus(TextualConvention, Integer32):
    description = "Virtual-chassis chassis status: \n                        init(0): init state\n                        running(1): running state\n                        invalidChassisId(2): invalid chassis id in vcsetup.cfg file\n                        helloDown(3): hello down\n                        duplicateChassisId(4): duplicate chassis id\n                        mismatchImage(5): images cross chassis are mismatching\n                        mismatchChassisType(6): slave's chassis type is different compared to the master's value\n                        mismatchHelloInterval(7): slave's hello interval is different compared to the master's value\n                        mismatchControlVlan(8): slave's control VLAN is different compared to the master's value\n                        mismatchGroup(9): slave's chassis group is different compared to the master's value\n                        mismatchLicenseConfig(10): slave's license settings are different compared to the master's value\n                        invalidLicense(11): invalid license settings\n                        splitTopology(12): the topology was split and the slave chassis became isolated from the master\n                        commandShutdown(13): chassis shutdown initiated by explicit management command\n                        failureShutdown(14): chassis shutdown triggered by a serious initialization failure"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("init", 0), ("running", 1), ("invalidChassisId", 2), ("helloDown", 3), ("duplicateChassisId", 4), ("mismatchImage", 5), ("mismatchChassisType", 6), ("mismatchHelloInterval", 7), ("mismatchControlVlan", 8), ("mismatchGroup", 9), ("mismatchLicenseConfig", 10), ("invalidLicense", 11), ("splitTopology", 12), ("commandShutdown", 13), ("failureShutdown", 14))

class VirtualChassisGroup(TextualConvention, Integer32):
    description = 'Virtual Chassis group.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class VirtualChassisPriority(TextualConvention, Integer32):
    description = 'Virtual Chassis priority.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class VirtualChassisSlotResetStatus(TextualConvention, Integer32):
    description = 'Virtual-chassis slot reset status: \n                         supported(0): This slot can be reset without spliting virtual chassis setup\n                         split(1): Reset this slot will split virtual chassis setup\n                         '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("supported", 0), ("split", 1))

class VirtualChassisType(TextualConvention, Integer32):
    description = 'Virtual-chassis chassis type: \n                        invalid(0): Only support Rushmore, Tor, Shasta, Medora, Everest \n                        rushmore(1): OS10k\n                        tor(2): OS6900\n                        shasta(3): OS6860\n                        medora(4): OS9900\n                        everest(5): OS6865\n                         '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("invalid", 0), ("rushmore", 1), ("tor", 2), ("shasta", 3), ("medora", 4), ("everest", 5))

class VirtualChassisVflSpeedType(TextualConvention, Integer32):
    description = 'Virtual-chassis VFL speed type: \n                        unassigned(0): VFL speed type is unassigned   \n                        unkown(1): VFL speed is unknown\n                        mismatch(2): This VFL has member ports operating at different speeds \n                        tenGB(3): All member ports of this VFL are operating at 10 Gbps\n                        fourtyGB(4): All member ports of this VFL are operating at 40 Gbps\n                        twentyOneGB(5): All member ports of this VFL are operating at 21 Gbps\n                         '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("unassigned", 0), ("unknown", 1), ("mismatch", 2), ("tenGB", 3), ("fortyGB", 4), ("twentyOneGB", 5))

class VirtualChassisVflMode(TextualConvention, Integer32):
    description = 'Virtual-chassis VFL mode: \n                        static(1): user needs to manually configure vfl and associated vfl member port   \n                        auto(2): vfl id will be automatically assigned to proper vfl member port\n                         '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("static", 1), ("auto", 2))

virtualChassisLocalInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 1))
virtualChassisLocalInfoChasId = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 1, 1), VirtualOperChassisId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisLocalInfoChasId.setStatus('current')
if mibBuilder.loadTexts: virtualChassisLocalInfoChasId.setDescription('Virtual Chassis Local chassis ID')
virtualChassisGlobalTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2), )
if mibBuilder.loadTexts: virtualChassisGlobalTable.setStatus('current')
if mibBuilder.loadTexts: virtualChassisGlobalTable.setDescription('Virtual Chassis Global Table')
virtualChassisGlobalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1), ).setIndexNames((0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"))
if mibBuilder.loadTexts: virtualChassisGlobalEntry.setStatus('current')
if mibBuilder.loadTexts: virtualChassisGlobalEntry.setDescription('Virtual Chassis Global Table Entry')
virtualChassisOperChasId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 1), VirtualOperChassisId())
if mibBuilder.loadTexts: virtualChassisOperChasId.setStatus('current')
if mibBuilder.loadTexts: virtualChassisOperChasId.setDescription('Operational Virtual-Chassis chassis ID.')
virtualChassisConfigChassisId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 2), VirtualConfigChassisId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: virtualChassisConfigChassisId.setStatus('current')
if mibBuilder.loadTexts: virtualChassisConfigChassisId.setDescription('Configured Virtual-Chassis chassis ID.\n        : This object can be configured for the local chassis or for a specific chassis.')
virtualChassisRole = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 3), VirtualChassisRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisRole.setStatus('current')
if mibBuilder.loadTexts: virtualChassisRole.setDescription('Virtual-Chassis chassis role')
virtualChassisPreviousRole = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 4), VirtualChassisRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisPreviousRole.setStatus('current')
if mibBuilder.loadTexts: virtualChassisPreviousRole.setDescription('Virtual-Chassis previous chassis role')
virtualChassisStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 5), VirtualChassisStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisStatus.setStatus('current')
if mibBuilder.loadTexts: virtualChassisStatus.setDescription('Virtual-Chassis chassis status')
virtualChassisOperPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 6), VirtualChassisPriority()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisOperPriority.setStatus('current')
if mibBuilder.loadTexts: virtualChassisOperPriority.setDescription('Virtual-Chassis operational chassis priority')
virtualChassisConfigPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 7), VirtualChassisPriority().clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: virtualChassisConfigPriority.setStatus('current')
if mibBuilder.loadTexts: virtualChassisConfigPriority.setDescription('Virtual-Chassis configured chassis priority\n        This object can be configured for the local chassis and for a specific chassis.')
virtualChassisGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 8), VirtualChassisGroup()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: virtualChassisGroup.setStatus('current')
if mibBuilder.loadTexts: virtualChassisGroup.setDescription('Virtual-Chassis chassis group.\n        When a master chassis is present in the topology, the chassis group can only be configured according to the following rules:\n        1. With exactly the same chassis group value as the current master chassis when the configuration applies to a single and specific chassis.   \n        2. With any value within the valid range as long as the configuration applies to all chassis at the same time.')
virtualChassisMac = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 9), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisMac.setStatus('current')
if mibBuilder.loadTexts: virtualChassisMac.setDescription('Virtual-Chassis chassis mac address.')
virtualChassisUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisUpTime.setStatus('current')
if mibBuilder.loadTexts: virtualChassisUpTime.setDescription('Virtual-Chassis chassis up time')
virtualChassisDesigNI = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 11), VirtualChassisNiSlot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisDesigNI.setStatus('current')
if mibBuilder.loadTexts: virtualChassisDesigNI.setDescription('Virtual-Chassis designated NI slot num')
virtualChassisPriCmm = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 12), VirtualChassisCmmSlot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisPriCmm.setStatus('current')
if mibBuilder.loadTexts: virtualChassisPriCmm.setDescription('Virtual-Chassis primary CMM slot num')
virtualChassisSecCmm = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 13), VirtualChassisCmmSlot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisSecCmm.setStatus('current')
if mibBuilder.loadTexts: virtualChassisSecCmm.setDescription('Virtual-Chassis secondary CMM slot num')
virtualChassisOperHelloInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 14), VirtualChassisHelloInterval().clone(10)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: virtualChassisOperHelloInterval.setStatus('current')
if mibBuilder.loadTexts: virtualChassisOperHelloInterval.setDescription('Operational Virtual-Chassis hello interval.')
virtualChassisOperControlVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 15), VirtualChassisControlVlan()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisOperControlVlan.setStatus('current')
if mibBuilder.loadTexts: virtualChassisOperControlVlan.setDescription('Operational Virtual-Chassis control VLAN.')
virtualChassisConfigHelloInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 16), VirtualChassisHelloInterval().clone(2)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: virtualChassisConfigHelloInterval.setStatus('deprecated')
if mibBuilder.loadTexts: virtualChassisConfigHelloInterval.setDescription('This is deprecated from release 7.3.3.R01.')
virtualChassisConfigControlVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 17), VirtualChassisControlVlan().clone(4094)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: virtualChassisConfigControlVlan.setStatus('current')
if mibBuilder.loadTexts: virtualChassisConfigControlVlan.setDescription('Configured Virtual-Chassis control VLAN.\n        This object can be configured for the local chassis, for a specific chassis and for all chassis.')
virtualChassisType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 18), VirtualChassisType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisType.setStatus('current')
if mibBuilder.loadTexts: virtualChassisType.setDescription('Virtual-Chassis chassis type')
virtualChassisLicense = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 19), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisLicense.setStatus('current')
if mibBuilder.loadTexts: virtualChassisLicense.setDescription('Virtual-Chassis chassis License string. A: Advanced; B: Data Center')
virtualChassisOperChasIdConsis = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 20), VirtualChassisConsistency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisOperChasIdConsis.setStatus('current')
if mibBuilder.loadTexts: virtualChassisOperChasIdConsis.setDescription('Virtual-Chassis consis status compared with master chassis')
virtualChassisConfigChasIdConsis = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 21), VirtualChassisConsistency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisConfigChasIdConsis.setStatus('current')
if mibBuilder.loadTexts: virtualChassisConfigChasIdConsis.setDescription('Virtual-Chassis consis status compared with master chassis')
virtualChassisOperControlVlanConsis = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 22), VirtualChassisConsistency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisOperControlVlanConsis.setStatus('current')
if mibBuilder.loadTexts: virtualChassisOperControlVlanConsis.setDescription('Virtual-Chassis consis status compared with master chassis')
virtualChassisConfigControlVlanConsis = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 23), VirtualChassisConsistency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisConfigControlVlanConsis.setStatus('current')
if mibBuilder.loadTexts: virtualChassisConfigControlVlanConsis.setDescription('Virtual-Chassis consis status compared with master chassis')
virtualChassisOperHelloIntervalConsis = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 24), VirtualChassisConsistency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisOperHelloIntervalConsis.setStatus('current')
if mibBuilder.loadTexts: virtualChassisOperHelloIntervalConsis.setDescription('Virtual-Chassis consis status compared hello interval with master chassis')
virtualChassisConfigHelloIntervalConsis = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 25), VirtualChassisConsistency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisConfigHelloIntervalConsis.setStatus('deprecated')
if mibBuilder.loadTexts: virtualChassisConfigHelloIntervalConsis.setDescription('This is deprecated from release 7.3.3.R01.')
virtualChassisChassisTypeConsis = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 26), VirtualChassisConsistency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisChassisTypeConsis.setStatus('current')
if mibBuilder.loadTexts: virtualChassisChassisTypeConsis.setDescription('Virtual-Chassis consis status compared with master chassis')
virtualChassisGroupConsis = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 27), VirtualChassisConsistency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisGroupConsis.setStatus('current')
if mibBuilder.loadTexts: virtualChassisGroupConsis.setDescription('Virtual-Chassis consis status compared with master chassis')
virtualChassisLicenseConsis = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 28), VirtualChassisConsistency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisLicenseConsis.setStatus('current')
if mibBuilder.loadTexts: virtualChassisLicenseConsis.setDescription('Virtual-Chassis consis status compared with master chassis')
virtualChassisGlobalConsis = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 29), VirtualChassisConsistency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisGlobalConsis.setStatus('current')
if mibBuilder.loadTexts: virtualChassisGlobalConsis.setDescription('Virtual-Chassis consis status compared with master chassis')
virtualChassisNumOfNeighbor = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisNumOfNeighbor.setStatus('current')
if mibBuilder.loadTexts: virtualChassisNumOfNeighbor.setDescription('Virtual-Chassis neighbor count')
virtualChassisNumOfDirectNeighbor = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 31), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisNumOfDirectNeighbor.setStatus('current')
if mibBuilder.loadTexts: virtualChassisNumOfDirectNeighbor.setDescription('Virtual-Chassis direct neighbor count')
virtualChassisVflMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 32), VirtualChassisVflMode().clone('static')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: virtualChassisVflMode.setStatus('current')
if mibBuilder.loadTexts: virtualChassisVflMode.setDescription('Virtual-Chassis vfl mode:        \n        static(0): user needs to manually configure vfl and associated vfl member port   \n        auto(1): vfl id will be automatically assigned to proper vfl member port')
virtualChassisNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 3), )
if mibBuilder.loadTexts: virtualChassisNeighborTable.setStatus('current')
if mibBuilder.loadTexts: virtualChassisNeighborTable.setDescription('Virtual Chassis Neighbor Table')
virtualChassisNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 3, 1), ).setIndexNames((0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"), (0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisNeighborChasId"))
if mibBuilder.loadTexts: virtualChassisNeighborEntry.setStatus('current')
if mibBuilder.loadTexts: virtualChassisNeighborEntry.setDescription('Virtual Chassis Neighbor Table Entry')
virtualChassisNeighborChasId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 3, 1, 1), VirtualOperChassisId())
if mibBuilder.loadTexts: virtualChassisNeighborChasId.setStatus('current')
if mibBuilder.loadTexts: virtualChassisNeighborChasId.setDescription('Virtual-Chassis Neighbor chassis ID.')
virtualChassisNeighborShortestPath = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 3, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisNeighborShortestPath.setStatus('current')
if mibBuilder.loadTexts: virtualChassisNeighborShortestPath.setDescription('Configured Virtual-Chassis neighbor shortest path. The format will be <chass_id>/<vfl_id>-><chass_id>/<vfl_id>-><chass_id>/<vfl_id>. EX: 2/0->1/0->3/1 ')
virtualChassisNeighborIsDirect = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 3, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisNeighborIsDirect.setStatus('current')
if mibBuilder.loadTexts: virtualChassisNeighborIsDirect.setDescription('To determine if this is a direct neighbor')
virtualChassisChassisResetListTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 4), )
if mibBuilder.loadTexts: virtualChassisChassisResetListTable.setStatus('current')
if mibBuilder.loadTexts: virtualChassisChassisResetListTable.setDescription('Virtual Chassis Chassis reset list Table')
virtualChassisChassisResetListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 4, 1), ).setIndexNames((0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"))
if mibBuilder.loadTexts: virtualChassisChassisResetListEntry.setStatus('current')
if mibBuilder.loadTexts: virtualChassisChassisResetListEntry.setDescription('Virtual Chassis Chassis Reset List Table Entry')
virtualChassisChassisResetList = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 4, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisChassisResetList.setStatus('current')
if mibBuilder.loadTexts: virtualChassisChassisResetList.setDescription('Indicate the chassis reset list.')
virtualChassisSlotResetStatusTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 5), )
if mibBuilder.loadTexts: virtualChassisSlotResetStatusTable.setStatus('current')
if mibBuilder.loadTexts: virtualChassisSlotResetStatusTable.setDescription('Virtual Chassis Slot reset Status Table')
virtualChassisSlotResetStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 5, 1), ).setIndexNames((0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"), (0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisSlotNum"))
if mibBuilder.loadTexts: virtualChassisSlotResetStatusEntry.setStatus('current')
if mibBuilder.loadTexts: virtualChassisSlotResetStatusEntry.setDescription('Virtual Chassis Slot Reset Status Table Entry')
virtualChassisSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 5, 1, 1), VirtualChassisNiSlot())
if mibBuilder.loadTexts: virtualChassisSlotNum.setStatus('current')
if mibBuilder.loadTexts: virtualChassisSlotNum.setDescription('Virtual-Chassis slot num.')
virtualChassisSlotResetStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 5, 1, 2), VirtualChassisSlotResetStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisSlotResetStatus.setStatus('current')
if mibBuilder.loadTexts: virtualChassisSlotResetStatus.setDescription('Virtual-Chassis slot reset status.')
virtualChassisVflTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6), )
if mibBuilder.loadTexts: virtualChassisVflTable.setStatus('current')
if mibBuilder.loadTexts: virtualChassisVflTable.setDescription('Virtual Chassis Virtual Fabric Link Table\n        This object can be configured for the local chassis or for a specific chassis.')
virtualChassisVflEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1), ).setIndexNames((0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"), (0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflId"))
if mibBuilder.loadTexts: virtualChassisVflEntry.setStatus('current')
if mibBuilder.loadTexts: virtualChassisVflEntry.setDescription('Virtual Chassis Virtual Fabric Link Table Entry')
virtualChassisVflId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 1), VirtualChassisVflId())
if mibBuilder.loadTexts: virtualChassisVflId.setStatus('current')
if mibBuilder.loadTexts: virtualChassisVflId.setDescription('Virtual Fabric Link Interface IfIndex')
virtualChassisVflDefaultVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: virtualChassisVflDefaultVlan.setStatus('deprecated')
if mibBuilder.loadTexts: virtualChassisVflDefaultVlan.setDescription('Virtual Fabric Link default vlan')
virtualChassisVflOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disabled", 0), ("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisVflOperStatus.setStatus('current')
if mibBuilder.loadTexts: virtualChassisVflOperStatus.setDescription('Virtual Fabric Link Operational Status')
virtualChassisVflPrimaryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisVflPrimaryPort.setStatus('current')
if mibBuilder.loadTexts: virtualChassisVflPrimaryPort.setDescription('Virtual Fabric Link primary Port ifindex. 0 is for default value when virtual fabric link is not up')
virtualChassisVflActivePortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisVflActivePortNum.setStatus('current')
if mibBuilder.loadTexts: virtualChassisVflActivePortNum.setDescription('Number of active member ports of participating on the Virtual Fabric Link.')
virtualChassisVflConfigPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisVflConfigPortNum.setStatus('current')
if mibBuilder.loadTexts: virtualChassisVflConfigPortNum.setDescription('Number of ports configured as members of the Virtual Fabric Link.')
virtualChassisVflRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: virtualChassisVflRowStatus.setStatus('current')
if mibBuilder.loadTexts: virtualChassisVflRowStatus.setDescription('Virtual Fabric Link RowStatus for creationh and deletion')
virtualChassisVflDirectNeighborChasId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 8), VirtualOperChassisId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisVflDirectNeighborChasId.setStatus('current')
if mibBuilder.loadTexts: virtualChassisVflDirectNeighborChasId.setDescription('The Chassis ID of the direct neighbor that is reachable via this VFL link,\n         or 0 if no neighbor.')
virtualChassisVflSpeedType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 9), VirtualChassisVflSpeedType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisVflSpeedType.setStatus('current')
if mibBuilder.loadTexts: virtualChassisVflSpeedType.setDescription('Virtual Fabric Link speed type')
virtualChassisVflMemberPortTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 7), )
if mibBuilder.loadTexts: virtualChassisVflMemberPortTable.setStatus('current')
if mibBuilder.loadTexts: virtualChassisVflMemberPortTable.setDescription('Virtual Fabric Link Member Port Table.\n        This object can be configured for the local chassis or for a specific chassis.')
virtualChassisVflMemberPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 7, 1), ).setIndexNames((0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"), (0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflId"), (0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortIfindex"))
if mibBuilder.loadTexts: virtualChassisVflMemberPortEntry.setStatus('current')
if mibBuilder.loadTexts: virtualChassisVflMemberPortEntry.setDescription('Virtual Fabric Link Member Port Table Entry.')
virtualChassisVflMemberPortIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 7, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: virtualChassisVflMemberPortIfindex.setStatus('current')
if mibBuilder.loadTexts: virtualChassisVflMemberPortIfindex.setDescription('Virtual Fabric Link Member Port ifIndex.')
virtualChassisVflMemberPortIsPrimay = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 7, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisVflMemberPortIsPrimay.setStatus('current')
if mibBuilder.loadTexts: virtualChassisVflMemberPortIsPrimay.setDescription('To determine if this Virtual Fabric Link Member Port is primary or not')
virtualChassisVflMemberPortOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disabled", 0), ("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisVflMemberPortOperStatus.setStatus('current')
if mibBuilder.loadTexts: virtualChassisVflMemberPortOperStatus.setDescription('Virtual Fabric Link Member Port operational status')
virtualChassisVflMemberPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 7, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: virtualChassisVflMemberPortRowStatus.setStatus('current')
if mibBuilder.loadTexts: virtualChassisVflMemberPortRowStatus.setDescription('Virtual Fabric Link Member Port RowStatus for creation and deletion')
virtualChassisTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 8))
virtualChassisDiagnostic = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 8, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("duplexMode", 1), ("speed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisDiagnostic.setStatus('current')
if mibBuilder.loadTexts: virtualChassisDiagnostic.setDescription('Indicates why a port configured as virtual-fabric member is unable to join the virtual-fabric link')
virtualChassisUpgradeCompleteStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 8, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("success", 1), ("failure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisUpgradeCompleteStatus.setStatus('current')
if mibBuilder.loadTexts: virtualChassisUpgradeCompleteStatus.setDescription('Indicates whether the software upgrade process has failed after a timeout or completed successfully.\n        Note that if the process fails, it may be still possible for the system to recover if the process\n        successfully completes later after the expired timeout.')
virtualChassisAutoVflPortTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 9), )
if mibBuilder.loadTexts: virtualChassisAutoVflPortTable.setStatus('current')
if mibBuilder.loadTexts: virtualChassisAutoVflPortTable.setDescription('Auto Virtual Fabric Link Port Table.')
virtualChassisAutoVflPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 9, 1), ).setIndexNames((0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisAutoVflPortIfindex"))
if mibBuilder.loadTexts: virtualChassisAutoVflPortEntry.setStatus('current')
if mibBuilder.loadTexts: virtualChassisAutoVflPortEntry.setDescription('Virtual Fabric Link Member Port Table Entry.')
virtualChassisAutoVflPortIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 9, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: virtualChassisAutoVflPortIfindex.setStatus('current')
if mibBuilder.loadTexts: virtualChassisAutoVflPortIfindex.setDescription('Auto virtual Fabric Link Member Port ifIndex.')
virtualChassisAutoVflIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 9, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisAutoVflIfindex.setStatus('current')
if mibBuilder.loadTexts: virtualChassisAutoVflIfindex.setDescription('Virtual Fabric Link ifIndex which is automatically assigned to this member port')
virtualChassisAutoVflPortMemberStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("unassigned", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisAutoVflPortMemberStatus.setStatus('current')
if mibBuilder.loadTexts: virtualChassisAutoVflPortMemberStatus.setDescription('Auto Virtual Fabric Link Port Member Port operational status')
virtualChassisAutoVflPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 9, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: virtualChassisAutoVflPortRowStatus.setStatus('current')
if mibBuilder.loadTexts: virtualChassisAutoVflPortRowStatus.setDescription('Auto Virtual Fabric Link Port RowStatus for creation and deletion')
virtualChassisStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 0, 1)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisStatus"))
if mibBuilder.loadTexts: virtualChassisStatusChange.setStatus('current')
if mibBuilder.loadTexts: virtualChassisStatusChange.setDescription('Critical trap indicates chassis status change.')
virtualChassisRoleChange = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 0, 2)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisRole"))
if mibBuilder.loadTexts: virtualChassisRoleChange.setStatus('current')
if mibBuilder.loadTexts: virtualChassisRoleChange.setDescription('Critical trap indicates chassis role change.')
virtualChassisVflStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 0, 3)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflOperStatus"))
if mibBuilder.loadTexts: virtualChassisVflStatusChange.setStatus('current')
if mibBuilder.loadTexts: virtualChassisVflStatusChange.setDescription('Critical trap indicates vflink status change.')
virtualChassisVflMemberPortStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 0, 4)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortIfindex"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortOperStatus"))
if mibBuilder.loadTexts: virtualChassisVflMemberPortStatusChange.setStatus('deprecated')
if mibBuilder.loadTexts: virtualChassisVflMemberPortStatusChange.setDescription('This trap is been deprecated since 7.3.3.R01.')
virtualChassisVflMemberPortJoinFailure = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 0, 5)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortIfindex"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisDiagnostic"))
if mibBuilder.loadTexts: virtualChassisVflMemberPortJoinFailure.setStatus('current')
if mibBuilder.loadTexts: virtualChassisVflMemberPortJoinFailure.setDescription('Major trap indicates a port configured as virtual-fabric member is unable to join the virtual-fabric link.')
virtualChassisUpgradeComplete = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 0, 6)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisUpgradeCompleteStatus"))
if mibBuilder.loadTexts: virtualChassisUpgradeComplete.setStatus('current')
if mibBuilder.loadTexts: virtualChassisUpgradeComplete.setDescription('Critical trap that indicates whether the software upgrade process has failed after a timeout or completed successfully.\n                Note that if the process fails, it may be still possible for the system to recover if the process\n                successfully completes later after the expired timeout.')
virtualChassisVflSpeedTypeChange = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 0, 7)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflSpeedType"))
if mibBuilder.loadTexts: virtualChassisVflSpeedTypeChange.setStatus('current')
if mibBuilder.loadTexts: virtualChassisVflSpeedTypeChange.setDescription('Critical trap indicates whenever vfl speed type is changed.')
alcatelIND1VirtualChassisMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisLocalInfoGroup"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisGlobalGroup"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisNeighborGroup"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisChassisResetListGroup"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisSlotRestStatusGroup"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflGroup"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1VirtualChassisMIBCompliance = alcatelIND1VirtualChassisMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIBCompliance.setDescription('Compliance statement for Virtual-Chassis Supervision.')
virtualChassisLocalInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisLocalInfoChasId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    virtualChassisLocalInfoGroup = virtualChassisLocalInfoGroup.setStatus('current')
if mibBuilder.loadTexts: virtualChassisLocalInfoGroup.setDescription('Chassis Supervision Virtual-Chassis Config Group.')
virtualChassisGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 2)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisConfigChassisId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisRole"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisPreviousRole"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisStatus"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperPriority"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisConfigPriority"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisGroup"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisMac"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisUpTime"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisDesigNI"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisPriCmm"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisSecCmm"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperHelloInterval"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperControlVlan"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisConfigHelloInterval"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisConfigControlVlan"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisType"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisLicense"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasIdConsis"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisConfigChasIdConsis"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperControlVlanConsis"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisConfigControlVlanConsis"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperHelloIntervalConsis"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisConfigHelloIntervalConsis"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisChassisTypeConsis"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisGroupConsis"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisLicenseConsis"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisGlobalConsis"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisNumOfNeighbor"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisNumOfDirectNeighbor"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    virtualChassisGlobalGroup = virtualChassisGlobalGroup.setStatus('current')
if mibBuilder.loadTexts: virtualChassisGlobalGroup.setDescription('Chassis Supervision Virtual-Chassis Config Group.')
virtualChassisNeighborGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 3)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisNeighborShortestPath"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisNeighborIsDirect"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    virtualChassisNeighborGroup = virtualChassisNeighborGroup.setStatus('current')
if mibBuilder.loadTexts: virtualChassisNeighborGroup.setDescription('Chassis Supervision Virtual-Chassis neighbor Group.')
virtualChassisChassisResetListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 4)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisChassisResetList"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    virtualChassisChassisResetListGroup = virtualChassisChassisResetListGroup.setStatus('current')
if mibBuilder.loadTexts: virtualChassisChassisResetListGroup.setDescription('Chassis Supervision Virtual-Chassis chassis reset list Group.')
virtualChassisSlotRestStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 5)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisSlotResetStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    virtualChassisSlotRestStatusGroup = virtualChassisSlotRestStatusGroup.setStatus('current')
if mibBuilder.loadTexts: virtualChassisSlotRestStatusGroup.setDescription('Chassis Supervision Virtual-Chassis slot reset statusGroup.')
virtualChassisVflGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 6)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflDefaultVlan"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflOperStatus"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflPrimaryPort"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflActivePortNum"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflConfigPortNum"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflRowStatus"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflDirectNeighborChasId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflSpeedType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    virtualChassisVflGroup = virtualChassisVflGroup.setStatus('current')
if mibBuilder.loadTexts: virtualChassisVflGroup.setDescription('Chassis Supervision Virtual-Chassis Vfl Group.')
virtualChassisVflMemberPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 7)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortIsPrimay"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortOperStatus"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    virtualChassisVflMemberPortGroup = virtualChassisVflMemberPortGroup.setStatus('current')
if mibBuilder.loadTexts: virtualChassisVflMemberPortGroup.setDescription('Chassis Supervision Virtual-Chassis Vfl Member Port Group.')
virtualChassisTrapInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 8)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisDiagnostic"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisUpgradeCompleteStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    virtualChassisTrapInfoGroup = virtualChassisTrapInfoGroup.setStatus('current')
if mibBuilder.loadTexts: virtualChassisTrapInfoGroup.setDescription('Chassis Supervision Virtual-Chassis trap info Group.')
virtualChassisTrapOBJGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 9)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisStatusChange"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisRoleChange"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflStatusChange"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortStatusChange"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortJoinFailure"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisUpgradeComplete"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflSpeedTypeChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    virtualChassisTrapOBJGroup = virtualChassisTrapOBJGroup.setStatus('current')
if mibBuilder.loadTexts: virtualChassisTrapOBJGroup.setDescription('Chassis Supervision Virtual-Chassis trap object Group.')
virtualChassisAutoVflPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 10)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisAutoVflIfindex"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisAutoVflPortMemberStatus"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisAutoVflPortRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    virtualChassisAutoVflPortGroup = virtualChassisAutoVflPortGroup.setStatus('current')
if mibBuilder.loadTexts: virtualChassisAutoVflPortGroup.setDescription('Auto Virtual-Chassis Vfl Port Group.')
mibBuilder.exportSymbols("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", virtualChassisGroup=virtualChassisGroup, VirtualChassisVflSpeedType=VirtualChassisVflSpeedType, VirtualChassisSlotResetStatus=VirtualChassisSlotResetStatus, alcatelIND1VirtualChassisMIBGroups=alcatelIND1VirtualChassisMIBGroups, VirtualChassisGroup=VirtualChassisGroup, alcatelIND1VirtualChassisMIBCompliances=alcatelIND1VirtualChassisMIBCompliances, virtualChassisChassisTypeConsis=virtualChassisChassisTypeConsis, virtualChassisUpgradeCompleteStatus=virtualChassisUpgradeCompleteStatus, virtualChassisConfigChassisId=virtualChassisConfigChassisId, alcatelIND1VirtualChassisMIBObjects=alcatelIND1VirtualChassisMIBObjects, VirtualChassisPriority=VirtualChassisPriority, virtualChassisConfigHelloInterval=virtualChassisConfigHelloInterval, virtualChassisChassisResetListTable=virtualChassisChassisResetListTable, virtualChassisVflRowStatus=virtualChassisVflRowStatus, VirtualChassisConsistency=VirtualChassisConsistency, virtualChassisNumOfNeighbor=virtualChassisNumOfNeighbor, virtualChassisConfigControlVlanConsis=virtualChassisConfigControlVlanConsis, VirtualChassisType=VirtualChassisType, virtualChassisChassisResetListEntry=virtualChassisChassisResetListEntry, virtualChassisSlotRestStatusGroup=virtualChassisSlotRestStatusGroup, virtualChassisVflId=virtualChassisVflId, virtualChassisVflMemberPortIfindex=virtualChassisVflMemberPortIfindex, virtualChassisConfigPriority=virtualChassisConfigPriority, virtualChassisVflMemberPortEntry=virtualChassisVflMemberPortEntry, virtualChassisRoleChange=virtualChassisRoleChange, virtualChassisMac=virtualChassisMac, virtualChassisDesigNI=virtualChassisDesigNI, virtualChassisNumOfDirectNeighbor=virtualChassisNumOfDirectNeighbor, virtualChassisVflTable=virtualChassisVflTable, virtualChassisGlobalConsis=virtualChassisGlobalConsis, VirtualChassisControlVlan=VirtualChassisControlVlan, virtualChassisOperHelloIntervalConsis=virtualChassisOperHelloIntervalConsis, alcatelIND1VirtualChassisMIB=alcatelIND1VirtualChassisMIB, virtualChassisLocalInfoGroup=virtualChassisLocalInfoGroup, virtualChassisOperChasId=virtualChassisOperChasId, virtualChassisOperControlVlanConsis=virtualChassisOperControlVlanConsis, virtualChassisVflSpeedType=virtualChassisVflSpeedType, virtualChassisType=virtualChassisType, VirtualChassisNiSlot=VirtualChassisNiSlot, virtualChassisLocalInfo=virtualChassisLocalInfo, virtualChassisAutoVflPortEntry=virtualChassisAutoVflPortEntry, VirtualChassisVflId=VirtualChassisVflId, virtualChassisChassisResetList=virtualChassisChassisResetList, VirtualChassisVflMode=VirtualChassisVflMode, virtualChassisGlobalGroup=virtualChassisGlobalGroup, virtualChassisOperHelloInterval=virtualChassisOperHelloInterval, virtualChassisTrapInfoGroup=virtualChassisTrapInfoGroup, alcatelIND1VirtualChassisMIBConformance=alcatelIND1VirtualChassisMIBConformance, virtualChassisLicense=virtualChassisLicense, virtualChassisAutoVflPortRowStatus=virtualChassisAutoVflPortRowStatus, virtualChassisAutoVflPortGroup=virtualChassisAutoVflPortGroup, virtualChassisStatus=virtualChassisStatus, virtualChassisConfigHelloIntervalConsis=virtualChassisConfigHelloIntervalConsis, virtualChassisVflOperStatus=virtualChassisVflOperStatus, virtualChassisNeighborIsDirect=virtualChassisNeighborIsDirect, virtualChassisVflDefaultVlan=virtualChassisVflDefaultVlan, virtualChassisAutoVflPortTable=virtualChassisAutoVflPortTable, virtualChassisVflActivePortNum=virtualChassisVflActivePortNum, alcatelIND1VirtualChassisMIBVCSP=alcatelIND1VirtualChassisMIBVCSP, VirtualChassisRole=VirtualChassisRole, virtualChassisVflEntry=virtualChassisVflEntry, virtualChassisVflMemberPortOperStatus=virtualChassisVflMemberPortOperStatus, virtualChassisVflMemberPortIsPrimay=virtualChassisVflMemberPortIsPrimay, virtualChassisTrapInfo=virtualChassisTrapInfo, virtualChassisVflStatusChange=virtualChassisVflStatusChange, virtualChassisGlobalTable=virtualChassisGlobalTable, virtualChassisNeighborEntry=virtualChassisNeighborEntry, virtualChassisVflMemberPortGroup=virtualChassisVflMemberPortGroup, virtualChassisPriCmm=virtualChassisPriCmm, virtualChassisAutoVflIfindex=virtualChassisAutoVflIfindex, virtualChassisGlobalEntry=virtualChassisGlobalEntry, alcatelIND1VirtualChassisMIBNotifications=alcatelIND1VirtualChassisMIBNotifications, virtualChassisConfigChasIdConsis=virtualChassisConfigChasIdConsis, virtualChassisSlotNum=virtualChassisSlotNum, VirtualChassisStatus=VirtualChassisStatus, virtualChassisUpTime=virtualChassisUpTime, VirtualChassisCmmSlot=VirtualChassisCmmSlot, virtualChassisVflMemberPortRowStatus=virtualChassisVflMemberPortRowStatus, virtualChassisSecCmm=virtualChassisSecCmm, virtualChassisNeighborChasId=virtualChassisNeighborChasId, virtualChassisVflGroup=virtualChassisVflGroup, virtualChassisSlotResetStatusEntry=virtualChassisSlotResetStatusEntry, virtualChassisVflMemberPortStatusChange=virtualChassisVflMemberPortStatusChange, virtualChassisVflMemberPortJoinFailure=virtualChassisVflMemberPortJoinFailure, virtualChassisChassisResetListGroup=virtualChassisChassisResetListGroup, VirtualOperChassisId=VirtualOperChassisId, virtualChassisSlotResetStatusTable=virtualChassisSlotResetStatusTable, virtualChassisVflConfigPortNum=virtualChassisVflConfigPortNum, virtualChassisStatusChange=virtualChassisStatusChange, virtualChassisLocalInfoChasId=virtualChassisLocalInfoChasId, virtualChassisOperChasIdConsis=virtualChassisOperChasIdConsis, virtualChassisVflMode=virtualChassisVflMode, PYSNMP_MODULE_ID=alcatelIND1VirtualChassisMIB, virtualChassisVflMemberPortTable=virtualChassisVflMemberPortTable, virtualChassisOperPriority=virtualChassisOperPriority, virtualChassisConfigControlVlan=virtualChassisConfigControlVlan, virtualChassisVflDirectNeighborChasId=virtualChassisVflDirectNeighborChasId, VirtualConfigChassisId=VirtualConfigChassisId, virtualChassisNeighborGroup=virtualChassisNeighborGroup, virtualChassisTrapOBJGroup=virtualChassisTrapOBJGroup, virtualChassisVflPrimaryPort=virtualChassisVflPrimaryPort, virtualChassisDiagnostic=virtualChassisDiagnostic, virtualChassisUpgradeComplete=virtualChassisUpgradeComplete, virtualChassisRole=virtualChassisRole, virtualChassisAutoVflPortMemberStatus=virtualChassisAutoVflPortMemberStatus, virtualChassisPreviousRole=virtualChassisPreviousRole, virtualChassisNeighborTable=virtualChassisNeighborTable, virtualChassisNeighborShortestPath=virtualChassisNeighborShortestPath, virtualChassisAutoVflPortIfindex=virtualChassisAutoVflPortIfindex, virtualChassisVflSpeedTypeChange=virtualChassisVflSpeedTypeChange, virtualChassisGroupConsis=virtualChassisGroupConsis, virtualChassisLicenseConsis=virtualChassisLicenseConsis, alcatelIND1VirtualChassisMIBCompliance=alcatelIND1VirtualChassisMIBCompliance, VirtualChassisHelloInterval=VirtualChassisHelloInterval, virtualChassisOperControlVlan=virtualChassisOperControlVlan, virtualChassisSlotResetStatus=virtualChassisSlotResetStatus)
