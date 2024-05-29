#
# PySNMP MIB module A4400-CPU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/alcatel/A4400-CPU-MIB
# Produced by pysmi-1.1.12 at Wed May 29 07:57:53 2024
# On host fv-az1024-251 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, IpAddress, NotificationType, Counter64, ObjectIdentity, Counter32, ModuleIdentity, Unsigned32, TimeTicks, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, enterprises, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "NotificationType", "Counter64", "ObjectIdentity", "Counter32", "ModuleIdentity", "Unsigned32", "TimeTicks", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "enterprises", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alcatel = MibIdentifier((1, 3, 6, 1, 4, 1, 637))
abs = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64))
a4400 = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 4400))
a4400CPU = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1))
pbxAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 1))
linux = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 1, 10))
unknown = MibIdentifier((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 1, 255))
pbxMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 0), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbxMibVersion.setStatus('mandatory')
if mibBuilder.loadTexts: pbxMibVersion.setDescription('The PBX MIB Version.')
pbxState = MibScalar((1, 3, 6, 1, 4, 1, 637, 64, 4400, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("indeterminate", 0), ("critical", 1), ("major", 2), ("minor", 3), ("warning", 4), ("normal", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pbxState.setStatus('mandatory')
if mibBuilder.loadTexts: pbxState.setDescription('The PBX state as defined by the trap manager.')
mibBuilder.exportSymbols("A4400-CPU-MIB", pbxAgent=pbxAgent, a4400=a4400, alcatel=alcatel, pbxState=pbxState, pbxMibVersion=pbxMibVersion, linux=linux, a4400CPU=a4400CPU, unknown=unknown, abs=abs)
