#
# PySNMP MIB module ALCATEL-IND1-IPMRM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nokia/aos7/ALCATEL-IND1-IPMRM-MIB
# Produced by pysmi-1.1.8 at Tue Jan 11 21:37:17 2022
# On host fv-az74-997 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
routingIND1Ipmrm, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "routingIND1Ipmrm")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, IpAddress, Bits, iso, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, MibIdentifier, Counter32, TimeTicks, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "Bits", "iso", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "MibIdentifier", "Counter32", "TimeTicks", "Counter64", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ALCATEL-IND1-IPMRM-MIB", alaIpmrmExtendedBoundaryStatus=alaIpmrmExtendedBoundaryStatus, alaIpmrmMbrProtocolApps=alaIpmrmMbrProtocolApps, alcatelIND1IPMRMMIB=alcatelIND1IPMRMMIB, alaIpmrmCompliance=alaIpmrmCompliance, alcatelIND1IPMRMMIBCompliances=alcatelIND1IPMRMMIBCompliances, alcatelIND1IPMRMMIBConformance=alcatelIND1IPMRMMIBConformance, alaIpmrmFailoverHolddown=alaIpmrmFailoverHolddown, PYSNMP_MODULE_ID=alcatelIND1IPMRMMIB, alaIpmrmGlobalConfig=alaIpmrmGlobalConfig, alcatelIND1IPMRMMIBObjects=alcatelIND1IPMRMMIBObjects, alcatelIND1IPMRMMIBGroups=alcatelIND1IPMRMMIBGroups, alaIpmrmMbrStatus=alaIpmrmMbrStatus, alaIpmrmConfigMIBGroup=alaIpmrmConfigMIBGroup)
