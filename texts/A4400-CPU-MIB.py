#
# PySNMP MIB module A4400-CPU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/alcatel/A4400-CPU-MIB
# Produced by pysmi-1.1.8 at Thu Jan 27 21:03:32 2022
# On host fv-az74-168 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, enterprises, ObjectIdentity, Integer32, Unsigned32, TimeTicks, IpAddress, iso, Bits, Gauge32, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "enterprises", "ObjectIdentity", "Integer32", "Unsigned32", "TimeTicks", "IpAddress", "iso", "Bits", "Gauge32", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64")
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
mibBuilder.exportSymbols("A4400-CPU-MIB", a4400=a4400, pbxMibVersion=pbxMibVersion, abs=abs, alcatel=alcatel, unknown=unknown, a4400CPU=a4400CPU, pbxState=pbxState, linux=linux, pbxAgent=pbxAgent)
