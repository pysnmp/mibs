#
# PySNMP MIB module ALCATEL-IND1-IPMRM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nokia/aos7/ALCATEL-IND1-IPMRM-MIB
# Produced by pysmi-1.1.8 at Thu Jan 13 23:11:50 2022
# On host fv-az83-250 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
routingIND1Ipmrm, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "routingIND1Ipmrm")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
IpAddress, TimeTicks, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, Bits, Counter64, NotificationType, Gauge32, Integer32, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "Bits", "Counter64", "NotificationType", "Gauge32", "Integer32", "Counter32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alcatelIND1IPMRMMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1))
alcatelIND1IPMRMMIB.setRevisions(('2012-04-03 00:00', '2014-12-04 00:00',))
if mibBuilder.loadTexts: alcatelIND1IPMRMMIB.setLastUpdated('201412040000Z')
if mibBuilder.loadTexts: alcatelIND1IPMRMMIB.setOrganization('Alcatel-Lucent')
alcatelIND1IPMRMMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 1))
alaIpmrmGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 1, 1))
alaIpmrmMbrStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaIpmrmMbrStatus.setStatus('current')
alaIpmrmMbrProtocolApps = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 1, 1, 2), Bits().clone(namedValues=NamedValues(("dvmrp", 0), ("pim", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIpmrmMbrProtocolApps.setStatus('current')
alaIpmrmFailoverHolddown = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(80)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaIpmrmFailoverHolddown.setStatus('current')
alaIpmrmExtendedBoundaryStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaIpmrmExtendedBoundaryStatus.setStatus('current')
alcatelIND1IPMRMMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 2))
alcatelIND1IPMRMMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 2, 1))
alcatelIND1IPMRMMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 2, 2))
alaIpmrmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmConfigMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaIpmrmCompliance = alaIpmrmCompliance.setStatus('current')
alaIpmrmConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmMbrStatus"), ("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmMbrProtocolApps"), ("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmFailoverHolddown"), ("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmExtendedBoundaryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaIpmrmConfigMIBGroup = alaIpmrmConfigMIBGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-IPMRM-MIB", alaIpmrmCompliance=alaIpmrmCompliance, alcatelIND1IPMRMMIBObjects=alcatelIND1IPMRMMIBObjects, alaIpmrmMbrStatus=alaIpmrmMbrStatus, alaIpmrmFailoverHolddown=alaIpmrmFailoverHolddown, alcatelIND1IPMRMMIBCompliances=alcatelIND1IPMRMMIBCompliances, alaIpmrmMbrProtocolApps=alaIpmrmMbrProtocolApps, alaIpmrmGlobalConfig=alaIpmrmGlobalConfig, alcatelIND1IPMRMMIB=alcatelIND1IPMRMMIB, PYSNMP_MODULE_ID=alcatelIND1IPMRMMIB, alaIpmrmExtendedBoundaryStatus=alaIpmrmExtendedBoundaryStatus, alaIpmrmConfigMIBGroup=alaIpmrmConfigMIBGroup, alcatelIND1IPMRMMIBGroups=alcatelIND1IPMRMMIBGroups, alcatelIND1IPMRMMIBConformance=alcatelIND1IPMRMMIBConformance)
