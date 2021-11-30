#
# PySNMP MIB module SESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sagemcom/SESSION-MIB
# Produced by pysmi-1.1.3 at Tue Nov 30 13:46:57 2021
# On host fv-az77-605 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
SagemBoolean, = mibBuilder.importSymbols("EQUIPMENT-MIB", "SagemBoolean")
sagemDr, = mibBuilder.importSymbols("SAGEM-DR-MIB", "sagemDr")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, ObjectIdentity, MibIdentifier, IpAddress, Counter64, Bits, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "ObjectIdentity", "MibIdentifier", "IpAddress", "Counter64", "Bits", "Unsigned32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
session = ModuleIdentity((1, 3, 6, 1, 4, 1, 1038, 201))
if mibBuilder.loadTexts: session.setLastUpdated('0206110000Z')
if mibBuilder.loadTexts: session.setOrganization('SAGEM/DR Tolbiac Centre')
tLock = MibScalar((1, 3, 6, 1, 4, 1, 1038, 201, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tLock.setStatus('current')
sessionIp = MibScalar((1, 3, 6, 1, 4, 1, 1038, 201, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sessionIp.setStatus('current')
sessionType = MibScalar((1, 3, 6, 1, 4, 1, 1038, 201, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 0), ("snmp", 1), ("http", 2), ("telnet", 3), ("vt100", 4), ("tpiEmulated", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sessionType.setStatus('current')
tLockDefault = MibScalar((1, 3, 6, 1, 4, 1, 1038, 201, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tLockDefault.setStatus('current')
tInactivity = MibScalar((1, 3, 6, 1, 4, 1, 1038, 201, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tInactivity.setStatus('current')
savePending = MibScalar((1, 3, 6, 1, 4, 1, 1038, 201, 20), SagemBoolean()).setMaxAccess("readonly")
if mibBuilder.loadTexts: savePending.setStatus('current')
mibBuilder.exportSymbols("SESSION-MIB", PYSNMP_MODULE_ID=session, tLock=tLock, savePending=savePending, sessionIp=sessionIp, sessionType=sessionType, session=session, tLockDefault=tLockDefault, tInactivity=tInactivity)
