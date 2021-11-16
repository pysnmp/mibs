#
# PySNMP MIB module SESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sagemcom/SESSION-MIB
# Produced by pysmi-1.1.0 at Tue Nov 16 11:47:27 2021
# On host fv-az77-509 platform Linux version 5.11.0-1020-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
SagemBoolean, = mibBuilder.importSymbols("EQUIPMENT-MIB", "SagemBoolean")
sagemDr, = mibBuilder.importSymbols("SAGEM-DR-MIB", "sagemDr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, TimeTicks, Integer32, Counter32, Counter64, Gauge32, Bits, Unsigned32, MibIdentifier, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "Integer32", "Counter32", "Counter64", "Gauge32", "Bits", "Unsigned32", "MibIdentifier", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("SESSION-MIB", tInactivity=tInactivity, PYSNMP_MODULE_ID=session, sessionType=sessionType, tLock=tLock, sessionIp=sessionIp, tLockDefault=tLockDefault, savePending=savePending, session=session)
