#
# PySNMP MIB module A4400-CPU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/alcatel/A4400-CPU-MIB
# Produced by pysmi-1.1.10 at Fri Nov 10 13:19:23 2023
# On host fv-az1435-737 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter32, Unsigned32, Counter64, ModuleIdentity, NotificationType, MibIdentifier, enterprises, Bits, Gauge32, IpAddress, ObjectIdentity, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "Unsigned32", "Counter64", "ModuleIdentity", "NotificationType", "MibIdentifier", "enterprises", "Bits", "Gauge32", "IpAddress", "ObjectIdentity", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("A4400-CPU-MIB", a4400=a4400, alcatel=alcatel, pbxState=pbxState, pbxMibVersion=pbxMibVersion, pbxAgent=pbxAgent, unknown=unknown, a4400CPU=a4400CPU, abs=abs, linux=linux)
