#
# PySNMP MIB module CTRON-WEBVIEW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-WEBVIEW-MIB
# Produced by pysmi-1.1.12 at Tue May 28 12:34:24 2024
# On host fv-az768-311 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ctApplication, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctApplication")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Integer32, iso, ObjectIdentity, ModuleIdentity, Counter64, TimeTicks, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Integer32", "iso", "ObjectIdentity", "ModuleIdentity", "Counter64", "TimeTicks", "NotificationType", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctWebView = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4))
ctEwvConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1))
ctEwvStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 2))
ctEwvDocSupport = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1))
ctEwvDocSupportAdmin = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvDocSupportAdmin.setStatus('mandatory')
ctEwvDocSupportLocation = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvDocSupportLocation.setStatus('mandatory')
ctEwvDocSupportAdminUID = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvDocSupportAdminUID.setStatus('mandatory')
ctEwvDocSupportUsername = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvDocSupportUsername.setStatus('mandatory')
ctEwvDocSupportPassword = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvDocSupportPassword.setStatus('mandatory')
ctEwvSystemParameters = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 2))
ctEwvAuthScheme = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("basic", 2), ("digest", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvAuthScheme.setStatus('mandatory')
ctEwvAuthNonceValidCount = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvAuthNonceValidCount.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-WEBVIEW-MIB", ctEwvSystemParameters=ctEwvSystemParameters, ctEwvDocSupportLocation=ctEwvDocSupportLocation, ctEwvDocSupportAdmin=ctEwvDocSupportAdmin, ctEwvStatus=ctEwvStatus, ctEwvDocSupportAdminUID=ctEwvDocSupportAdminUID, ctEwvDocSupportUsername=ctEwvDocSupportUsername, ctEwvAuthScheme=ctEwvAuthScheme, ctEwvAuthNonceValidCount=ctEwvAuthNonceValidCount, ctEwvDocSupport=ctEwvDocSupport, ctWebView=ctWebView, ctEwvDocSupportPassword=ctEwvDocSupportPassword, ctEwvConfiguration=ctEwvConfiguration)
