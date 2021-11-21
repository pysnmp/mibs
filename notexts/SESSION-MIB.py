#
# PySNMP MIB module SESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sagemcom/SESSION-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 13:48:12 2021
# On host fv-az74-779 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
SagemBoolean, = mibBuilder.importSymbols("EQUIPMENT-MIB", "SagemBoolean")
sagemDr, = mibBuilder.importSymbols("SAGEM-DR-MIB", "sagemDr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, NotificationType, IpAddress, Bits, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, Gauge32, ObjectIdentity, Integer32, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "IpAddress", "Bits", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "Gauge32", "ObjectIdentity", "Integer32", "iso", "Counter64")
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
mibBuilder.exportSymbols("SESSION-MIB", tInactivity=tInactivity, tLock=tLock, sessionIp=sessionIp, session=session, sessionType=sessionType, PYSNMP_MODULE_ID=session, savePending=savePending, tLockDefault=tLockDefault)
