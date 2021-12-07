#
# PySNMP MIB module PRIV-VENDORDEF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRIV-VENDORDEF-MIB
# Produced by pysmi-1.1.3 at Tue Dec  7 16:54:25 2021
# On host fv-az42-142 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, IpAddress, Counter64, Integer32, Gauge32, MibIdentifier, Counter32, iso, enterprises, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "IpAddress", "Counter64", "Integer32", "Gauge32", "MibIdentifier", "Counter32", "iso", "enterprises", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
privateVendorOID = ModuleIdentity((1, 3, 6, 1, 4, 1, 738))
privateVendorOID.setRevisions(('2007-09-29 00:00',))
if mibBuilder.loadTexts: privateVendorOID.setLastUpdated('200709290000Z')
if mibBuilder.loadTexts: privateVendorOID.setOrganization('BATM Advanced Communication')
mibBuilder.exportSymbols("PRIV-VENDORDEF-MIB", privateVendorOID=privateVendorOID, PYSNMP_MODULE_ID=privateVendorOID)
